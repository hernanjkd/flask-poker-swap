from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80), nullable=False)
    last_name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=True, nullable=False)
    tournaments = db.relationship('Tournaments', lazy=True)
    swaps = db.relationship('Swaps', lazy=True)
    tournament_id = db.Column(db.Integer, db.ForeignKey('Tournaments.id'))

    def __repr__(self):
        return f'<Person {self.email}>'

    def serialize(self):
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
            "tournaments": list(map(lambda e: e.serialize(), self.tournaments)),
            "swaps": list(map(lambda e: e.serialize(), self.swaps))
        }


class Tournaments(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))
    status = db.Column(db.String(80)) # date that starts, in progress, finished
    results = db.Column(db.String(1000)) # 
    scheduled_date = db.Column(db.)
    players = db.relationship('Users', lazy=True)
    user_id = db.Column(db.Integer, db.ForeignKey('Users.id'))

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
    users = db.relationship('users')