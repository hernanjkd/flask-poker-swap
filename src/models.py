from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Users(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.Date, default=datetime.now())
    
    email = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=True, nullable=False)

    def __repr__(self):
        return f'<Users {self.email}>'

    def serialize(self):
        return {
            "id": self.id,
            "date_created": self.date_created,
            "email": self.email
        }



class Profiles(db.Model):
    __tablename__ = 'profiles'
    id = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key=True)
    date_created = db.Column(db.Date, default=datetime.now())

    first_name = db.Column(db.String(80), nullable=False)
    last_name = db.Column(db.String(80), nullable=False)

    user = db.relationship('Users', backref='profile', uselist=False)
    
    def __repr__(self):
        return f'<Profiles {self.first_name} {self.last_name}>'

    def serialize(self):
        return {
            "id": self.id,
            "date_created": self.date_created,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.user.email
        }
    


class Pictures(db.Model):
    __tablename__ = 'pictures'
    id = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key=True)
    date_created = db.Column(db.Date, default=datetime.now())

    def serialize(self):
        return {
            "id": self.id,
            "date_created": self.date_created
        }



class Tournaments(db.Model):
    __tablename__ = 'tournaments'
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.Date, default=datetime.now())

    name = db.Column(db.String(120))
    start_date = db.Column(db.Date)
    end_date = db.Column(db.Date)

    flights = db.relationship('Flights', back_populates='tournament')

    def __repr__(self):
        return f'<Tournament {self.name}>'

    def serialize(self):
        return {
            "id": self.id,
            "date_created": self.date_created,
            "name": self.name,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "flights": list(map(lambda e: e.serialize(), self.flights))
        }



class Flights(db.Model):
    __tablename__ = 'flights'
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.Date, default=datetime.now())

    start_date = db.Column(db.Date)
    end_date = db.Column(db.Date)

    tournament_id = db.Column(db.Integer, db.ForeignKey('tournaments.id'))
    tournament = db.relationship('Tournaments', back_populates='flights')

    def __repr__(self):
        return f'<Flights {self.tournament.name} {self.start_date} - {self.end_date}>'

    def serialize(self):
        return {
            "id": self.id,
            "date_created": self.date_created,
            "start_date": self.start_date,
            "end_date": self.end_date
        }



# tags = db.Table('tags',
#     db.Column('tag_id', db.Integer, db.ForeignKey('tag.id'), primary_key=True),
#     db.Column('page_id', db.Integer, db.ForeignKey('page.id'), primary_key=True)
# )

# class Page(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     tags = db.relationship('Tag', secondary=tags, lazy='subquery',
#         backref=db.backref('pages', lazy=True))

# class Tag(db.Model):
#     id = db.Column(db.Integer, primary_key=True)


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