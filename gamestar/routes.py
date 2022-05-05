"""Application Routes"""

import re
from flask import render_template, request, redirect, url_for, flash
from gamestar import app, db
from gamestar.models import User, Game, Review
from werkzeug.security import generate_password_hash


@app.route('/')
def home():
    """
    Render home.html template.
    """
    return render_template('home.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    """
    GET: Render register.html template.
    POST: Get form data for user registration. 
    If valid, store in User table in database.
    """
    if request.method == 'POST':
        username = request.form.get('username').lower().strip()
        password = request.form.get('password')
        password_confirm = request.form.get('confirm_password')

        if len(username) < 3 or len(username) > 16:
            flash('Registration Failed:\
                 Username must be between 3-16 characters in length.\
                      Please Try Again!')
            return render_template('register.html')

        if re.search('[^A-z0-9]', username):
            flash('Registration Failed:\
                 Username must only contain letters and numbers.\
                      Please Try Again!')
            return render_template('register.html')

        if password != password_confirm:
            flash('Registration Failed:\
                 Passwords do not match.\
                      Please Try Again!')
            return render_template('register.html')

        existing_user = User.query.filter(User.username == username).count()

        if existing_user > 0:
            flash('Registration Failed:\
                 Username taken.\
                      Please Try Again!')
            return render_template('register.html')

        password_hash = generate_password_hash(password)

        user = User(
            username=username, password=password_hash
            )
        db.session.add(user)
        db.session.commit()

    return render_template('register.html')
