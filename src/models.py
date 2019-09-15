from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Users(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.Date, default=datetime.now())
    # last_modified = db.Column(db.Date, onupdate=datetime.now())
    
    email = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=True, nullable=False)

    # profile = db.relationship('Profiles', lazy=True, uselist=False, backref='user_id')

    def serialize(self):
        return {
            "id": self.id,
            "date_created": self.date_created,
            "email": self.email
        }



class Profiles(db.Model):
    __tablename__ = 'profiles'
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=datetime.now)

    first_name = db.Column(db.String(80), nullable=False)
    last_name = db.Column(db.String(80), nullable=False)

    user = db.relationship('Users', backref='profile')
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    
    # email = db.Column(db.String(80), db.ForeignKey('Users.email'))
    # tournaments = db.relationship('Tournaments', lazy=True)
    # swaps = db.relationship('Swaps', lazy=True)
    # token_transactions = db.relationship('Token_Transactions', lazy=True)

    def serialize(self):
        return {
            "id": self.id,
            "date_created": self.date_created,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.user_id
            # "tokens": self.tokens,
            # "tournaments": list(map(lambda e: e.serialize(), self.tournaments)),
            # "swaps": list(map(lambda e: e.serialize(), self.swaps))
            # "token_transactions": list(map(lambda e: e.serialize(), self.token_transactions))
        }
    


# class Tournaments(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     date_created = db.Column(db.DateTime, default=datetime.now)

#     name = db.Column(db.String(120))
#     results = db.Column(db.String(1000))
#     start_date = db.Column(db.DateTime)
#     end_date = db.Column(db.DateTime)

#     players = db.relationship('Users', lazy=True)

#     def __repr__(self):
#         return f'<Tournament {self.name}>'

#     def serialize(self):
#         return {
#             "id": self.id,
#             "name": self.name,
#             "results": self.results,
#             "schedule": self.schedule,
#             "players": list(map(lambda e: e.serialize(), self.players))
#         }


# class Swaps(db.Model):
#     id = db.Column(db.Integer, primary_key=True)

#     amount_percentage = db.Column(db.Integer)
#     completed = db.Column(db.Boolean, default=False)

#     sender_id = db.Column(db.Integer, db.ForeignKey('Users.id'))
#     reciever_id = db.Column(db.Integer, db.ForeignKey('Users.id'))
#     tournament_id = db.Column(db.Integer, db.ForeignKey('Tournaments.id'))

#     def __repr__(self):
#         return f'<Swaps {self.id}>'

#     def serialize(self):
#         return {
#             "id": self.id,
#             "amount_percentage": self.amount_percentage,
#             "completed": self.completed
#             # "sender": 
#             # "reciever": 
#             # "tournament": 
#         }


# class Token_Transactions(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     amount = db.Column(db.Integer)

#     user_id = db.Column(db.Integer, db.ForeignKey('Users.id'))