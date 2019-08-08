
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from flask_jwt_simple import JWTManager, jwt_required, create_jwt, get_jwt_identity
from utils import APIException, generate_sitemap, verify_json
from models import db, Users, Login, Tournaments, Swaps

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_CONNECTION_STRING')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)

app.config['JWT_SECRET_KEY'] = '230130905682186130'
jwt = JWTManager(app)


@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

@app.route('/')
def sitemap():
    return generate_sitemap(app)

#############################################################################

@app.route('/login', methods=['POST'])
def login():
    body = request.get_json()

    if body is None:
        raise APIException("You need to specify the request body as a json object", status_code=400)
    if 'email' not in body:
        raise APIException('You need to specify the email', status_code=400)
    if 'password' not in body:
        raise APIException('You need to specify the username', status_code=400)

    if 

    return "ok", 200

#############################################################################

@app.route('/user', methods=['POST', 'GET'])
def handle_user():

    # Register User
    if request.method == 'POST':
        body = request.get_json()

        missing_item = verify_json(body)

        if missing_item:
            raise APIException("You need to specify the " + missing_item, status_code=400)

        if body is None:
            raise APIException("You need to specify the request body as a json object", status_code=400)
        if 'first_name' not in body:
            raise APIException('You need to specify the first_name', status_code=400)
        if 'last_name' not in body:
            raise APIException('You need to specify the last_name', status_code=400)
        if 'email' not in body:
            raise APIException('You need to specify the email', status_code=400)
        if 'password' not in body:
            raise APIException('You need to specify the password', status_code=400)

        obj = Users(first_name=body['first_name'], last_name=body['last_name'], 
                    email=body['email'], password=body['password'])
        db.session.add(obj)
        db.session.commit()
        return "ok", 200

    # GET request
    if request.method == 'GET':
        all_users = Users.query.all()
        all_users = list(map(lambda x: x.serialize(), all_users))
        return jsonify(all_users), 200

    return "Invalid Method", 404


@app.route('/user/<int:user_id>', methods=['PUT', 'GET', 'DELETE'])
def get_single_user(user_id):
    """
    Single user
    """

    # PUT request
    if request.method == 'PUT':
        body = request.get_json()
        if body is None:
            raise APIException("You need to specify the request body as a json object", status_code=400)

        obj = user.query.get(user_id)
        if obj is None:
            raise APIException('User not found', status_code=404)

        if "username" in body:
            obj.username = body["username"]
        if "email" in body:
            obj.email = body["email"]
        db.session.commit()

        return jsonify(obj.serialize()), 200

    # GET request
    if request.method == 'GET':
        obj = User.query.get(user_id)
        if obj is None:
            raise APIException('User not found', status_code=404)
        return jsonify(obj.serialize()), 200

    # DELETE request
    if request.method == 'DELETE':
        obj = user.query.get(user_id)
        if obj is None:
            raise APIException('User not found', status_code=404)
        db.session.delete(obj)
        db.session.commit()
        return "ok", 200

    return "Invalid Method", 404


if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT)
