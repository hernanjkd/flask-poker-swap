from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.Date, default=datetime.now)
    last_modified = db.Column(db.Date, onupdate=datetime.now())
    number = db.Column(db.Integer)

    def serialize(self):
        return {
            "id": self.id,
            "created": self.date_created,
            "updated": self.last_modified,
            "number": self.number
        }


# class Users(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     date_created = db.Column(db.Date, default=datetime.now())
#     last_modified = db.Column(db.Date, onupdate=datetime.now())

#     first_name = db.Column(db.String(80), nullable=False)
#     last_name = db.Column(db.String(80), nullable=False)
#     email = db.Column(db.String(80), unique=True, nullable=False)
#     password = db.Column(db.String(80), unique=True, nullable=False)
#     tokens = db.Column(db.Integer, default=0)

#     tournaments = db.relationship('Tournaments', lazy=True)
#     swaps = db.relationship('Swaps', lazy=True)
#     token_transactions = db.relationship('Token_Transactions', lazy=True)

#     def __repr__(self):
#         return f'<Person {self.email}>'

#     def serialize(self):
#         return {
#             "id": self.id,
#             "first_name": self.first_name,
#             "last_name": self.last_name,
#             "email": self.email,
#             "tokens": self.tokens,
#             "tournaments": list(map(lambda e: e.serialize(), self.tournaments)),
#             "swaps": list(map(lambda e: e.serialize(), self.swaps))
#             # "token_transactions": list(map(lambda e: e.serialize(), self.token_transactions))
#         }


# class Tournaments(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     # date_created = db.Column(db.DateTime, oncreate=datetime.datetime.now())
#     # last_modified = db.Column(db.DateTime, onupdate=func.utc_timestamp())

#     name = db.Column(db.String(120))
#     results = db.Column(db.String(1000))
#     schedule = db.Column(db.DateTime)
#     completed = db.Column(db.Boolean, default=False)

#     players = db.relationship('Users', lazy=True)

#     def __repr__(self):
#         return f'<Tournament {self.name}>'

#     def serialize(self):
#         return {
#             "id": self.id,
#             "name": self.name,
#             "results": self.results,
#             "schedule": self.schedule,
#             "completed": self.completed,
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