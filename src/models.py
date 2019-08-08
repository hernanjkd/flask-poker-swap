from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80), nullable=False)
    last_name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=True, nullable=False)
    tokens = db.Column(db.Integer, default=0)
    tournaments = db.relationship('Tournaments', lazy=True)
    swaps = db.relationship('Swaps', lazy=True)
    token_transactions = db.relationship('Token_Transactions', lazy=True)

    def __repr__(self):
        return f'<Person {self.email}>'

    def serialize(self):
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
            "tournaments": list(map(lambda e: e.serialize(), self.tournaments)),
            "swaps": list(map(lambda e: e.serialize(), self.swaps)),
            "tokens": self.tokens
            # "token_transactions": list(map(lambda e: e.serialize(), self.token_transactions))
        }


class Tournaments(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))
    completed = db.Column(db.Boolean)
    results = db.Column(db.String(1000))
    schedule = db.Column(db.DateTime)
    players = db.relationship('Users', lazy=True)

    def __repr__(self):
        return f'<Tournament {self.name}>'

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "players": list(map(lambda e: e.serialize(), self.players))
        }


class Swaps(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    amount_percentage = db.Column(db.Integer)
    status = db.Column()
    sender_id = db.Column(db.Integer, db.ForeignKey('Users.id'))
    reciever_id = db.Column(db.Integer, db.ForeignKey('Users.id'))
    tournament_id = db.Column(db.Integer, db.ForeignKey('Tournaments.id'))


class Token_Transactions(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('Users.id'))