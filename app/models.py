from enum import unique
from app import db


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    password_hash = db.Column(db.String(100), nullable=False)
    regexes = db.relationship('Regex', backref='user')

    def __repr__(self) -> str:
        return f'{self.id} - {self.username}'


class Regex(db.Model):
    __tablename__ = 'regexes'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    content = db.Column(db.String(1000), nullable=False)
    user_id = db.Column(db.Integer(), db.ForeignKey('users.id'))

    def __repr__(self) -> str:
        return f'Regex: {self.content}'