from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80), nullable=False)
    last_name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=True, nullable=False)
    login = db.relationship('Login', lazy=True)
    tournaments = db.relationship('Tournaments', lazy=True)
    swaps = db.relationship('Swaps', lazy=True)

    def __repr__(self):
        return f'<Person {self.username}>'

    def serialize(self, admin=False):
        if admin:
            return {
                "id": self.id,
                "first_name": self.first_name,
                "last_name": self.last_name,
                "email": self.email,
                "tournaments": list(map(lambda e: e.serialize(), self.tournaments)),
                "swaps": list(map(lambda e: e.serialize(), self.swaps))
            }
        return {
            "username": self.username
        }


class Tournaments(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    players = db.Column(db.Integer)

    def __repr__(self):
        return f'<Tournament {self.name}>'

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "players": self.players
        }


class Swaps(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    users = db.relationship('users')