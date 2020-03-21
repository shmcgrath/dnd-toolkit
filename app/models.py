from datetime import datetime
from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(128), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    player_characters = db.relationship('PlayerCharacter', backref='creator',
            lazy='dynamic')

    def __repr__(self):
        return '<User {}>'.format(self.username)

class PlayerCharacter(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    pc_class = db.Column(db.String(128))
    pc_race = db.Column(db.String(128))
    date_created = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post {}>'.format(self.name)
