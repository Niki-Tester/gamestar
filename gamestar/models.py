"""Flask SQL-Alchemy Database Models"""
import time
import math
from gamestar import db


class User(db.Model):
    """Schema for the User model"""
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(16), unique=True, nullable=False)
    password = db.Column(db.Text, nullable=False)

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return f'Id: {self.id} | Username: {self.username}'


class Game(db.Model):
    """Schema for the Task model"""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    artwork = db.Column(db.Text, nullable=False)
    summary = db.Column(db.Text, default=False, nullable=True)
    igdb_id = db.Column(db.Integer, unique=True, nullable=False)
    cover_art = db.Column(db.Text, nullable=False)

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return f'Id: {self.id} | Name: {self.name}'


class Review(db.Model):
    """Schema for the review model"""
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    game_id = db.Column(db.Integer, db.ForeignKey('game.id'), nullable=False)
    rating = db.Column(db.Float, nullable=False)
    heading = db.Column(db.Text, nullable=False)
    liked_text = db.Column(db.Text, nullable=False)
    disliked_text = db.Column(db.Text, nullable=False)
    hours = db.Column(db.Integer, nullable=False)
    likes = db.Column(db.Text, nullable=True)
    timestamp = db.Column(db.Integer,
                          nullable=False,
                          default=math.floor(time.time()))

    def __repr__(self):
        # __repr__ to represent itself in the for of a string
        return f'Id: {self.id} | User_Id: {self.user_id} | '\
               f'Game_Id: {self.game_id}'


class Twitch(db.Model):
    """Schema for the User model"""
    id = db.Column(db.Integer, primary_key=True)
    access_token = db.Column(db.String, nullable=False)
    expires_in = db.Column(db.Integer, nullable=False)
    token_type = db.Column(db.String, nullable=False)
    date_added = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return f'ID: {self.id} | '\
            f'Access Token: {self.access_token} | '\
            f'Expires In: {self.expires_in} | '\
            f'Token Type: {self.token_type} | '\
            f'Date Added: {self.date_added}'
