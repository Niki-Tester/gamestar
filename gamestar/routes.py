"""Application Routes"""

from flask import render_template
from gamestar import app, db
from gamestar.models import User, Game, Review


@app.route('/')
def home():
    """
    Render home.html template.
    """
    return render_template('home.html')


@app.route('/register')
def register():
    """
    GET: Render register.html template.
    POST: Get form data for user registration. 
    If valid, store in User table in database.
    """
    return render_template('register.html')
