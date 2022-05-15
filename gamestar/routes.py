"""Application Routes"""

import re
import random
import json
from flask import (render_template, request, redirect, url_for, flash,
                   session, jsonify)
from werkzeug.security import generate_password_hash, check_password_hash
from gamestar.igdb import (get_game_data_by_string, get_game_cover_art,
                           get_game_data_by_id, get_game_artwork)
from gamestar import app, db
from gamestar.models import User, Game, Review


@app.route('/')
def home():
    """
    Render home.html template.
    """
    games = Game.query.all()
    for game in games:
        reviews = Review.query.filter_by(game_id=game.id).all()
        total_rating = 0
        for review in reviews:
            total_rating += review.rating

        average_rating = total_rating / len(reviews)
        game.average_rating = average_rating

    return render_template('home.html', games=games, title='Home')


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

        existing_user = User.query.filter_by(username=username).first()

        if existing_user:
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

        session['username'] = user.username
        flash('Successfully Registered & Logged In!')
        return redirect(url_for('home'))

    return render_template('register.html', title='Register')


@app.route('/login', methods=['GET', 'POST'])
def login():
    """
    GET: Render login.html template.
    POST: Get form data for user login.
    If username/password match log user in and store in session.
    """
    if request.method == 'POST':
        username = request.form.get('username').lower().strip()
        password = request.form.get('password')

        existing_user = User.query.filter_by(username=username).first()

        if not existing_user:
            flash('Log In Failed:\
                 Username not found.\
                      Please Try Again!')
            return redirect(url_for('login'))

        if not check_password_hash(existing_user.password, password):
            flash('Log In Failed:\
                 Username/Password combination not recognized.\
                      Please Try Again!')
            return redirect(url_for('login'))

        session['username'] = existing_user.username
        flash('Successfully Logged In')
        return redirect(url_for('home'))

    return render_template('login.html', title='Login')


@app.route('/logout')
def logout():
    """
    Logs user out by clearing the session cookie.
    """
    try:
        if session['username']:
            session.clear()
            flash('Successfully Logged Out')
    except KeyError:
        print('User attempted to log out when not logged in.')

    return redirect(url_for('home'))


@app.route('/profile', methods=['GET', 'POST'])
def profile():
    """
    GET: Renders profile.html template
    POST: Gets form data for changing users password
    """
    # POST Request
    if request.method == 'POST':
        current_password = request.form.get('current')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')

        if password != confirm_password:
            flash('Password Change Failed:\
                 Passwords do not match.\
                      Please Try Again!')
            return redirect(url_for('profile'))

        existing_user = User.query.filter_by(
            username=session['username']).first()

        if not existing_user:
            flash('Password Change Failed:\
                 Username not found.\
                      Please Try Again!')
            return redirect(url_for('profile'))

        passwords_match = check_password_hash(
            existing_user.password, current_password)

        if not passwords_match:
            flash('Password Change Failed:\
                 Current Password incorrect.\
                      Please Try Again!')
            return redirect(url_for('profile'))

        existing_user.password = generate_password_hash(password)

        db.session.commit()
        flash('Password Changed Successfully')
        return redirect(url_for('profile'))

    # GET Request
    try:
        if session['username']:
            return render_template('profile.html', user=session['username'],
                                   title='Your Profile')
    except KeyError:
        print('User attempted to view profile while not logged in.')
        return redirect(url_for('home'))


@app.route('/profile/delete', methods=['GET', 'POST'])
def delete_user():
    """Delete user profile, and remove all user data"""

    # POST Request
    if request.method == 'POST':
        username = request.form.get('username')
        if username != session['username']:
            flash('Error deleting profile, '
                  'please contact an administrator')
            return redirect(url_for('profile'))

        flash('User profile successfully deleted!')
        return redirect(url_for('home'))

    # GET Request
    try:
        if session['username']:
            return redirect(url_for('profile'))
    except KeyError:
        print('User attempted to delete user while not logged in.')
        return redirect(url_for('home'))


@app.route('/manage', methods=['GET', 'POST'])
def manage():
    """
    GET: Renders manage.html template.
    Displaying reviews user has created if any.
    """
    try:
        if session['username']:
            user = User.query.filter_by(username=session['username']).first()
            reviews = Review.query.filter_by(user_id=user.id).all()
            user_reviews = []
            for review in reviews:
                game = Game.query.filter_by(id=review.game_id).first()
                user_reviews.append({
                                'game': game,
                                'review': review
                                })

            return render_template('manage.html', user_reviews=user_reviews,
                                   title='Your Reviews')
    except KeyError:
        print('User attempted to manage reviews when not logged in.')

    return redirect(url_for('home'))


@app.route('/search', methods=['GET', 'POST'])
def search():
    """
    GET: Renders search.html template.
    POST: Search IGDB by game name and return results
    """
    # POST:
    if request.method == 'POST':
        query = request.form.get('search')

        data = get_game_data_by_string(query)

        for game in data:
            if 'cover' in game:
                game['img_url'] = get_game_cover_art(game['id'])
            else:
                game['img_url'] = url_for('static',
                                          filename='images/no_cover.webp')

            game['form_action'] = url_for('add_review')

        return jsonify(data)

    # GET:
    try:
        if session['username']:
            return render_template('search.html', title='Search Games')
    except KeyError:
        print('User attempted to search games when not logged in.')

    return redirect(url_for('home'))


@app.route('/add_review', methods=['GET', 'POST'])
def add_review():
    """
    GET:    Redirects to /search
    POST:   1) Adds game to database if does not exist.
            2) Adds review to database.
    """

    # POST:
    if request.method == 'POST':
        game_id = request.form.get('game_id')
        game = get_game_data_by_id(game_id)[0]
        if 'cover' in game:
            game['cover'] = get_game_cover_art(game_id)
        else:
            game['cover'] = url_for('static', filename='images/no_cover.webp')

        game['artworks'] = get_game_artwork(game_id)

        if len(game['artworks']) > 0:
            return render_template('add_review.html',
                                   data=game,
                                   background=random.choice(game['artworks']),
                                   title='Create Review')

        return render_template('add_review.html', data=game,
                               title='Create Review')

    # GET:
    return redirect('search')


@app.route('/submit_review/<game_id>', methods=['POST'])
def submit_review(game_id):
    """
    Adds users review to database.
    """

    existing_game = Game.query.filter_by(igdb_id=game_id).first()

    if not existing_game:
        igdb_game_data = get_game_data_by_id(game_id)[0]
        igdb_game_artwork = get_game_artwork(game_id)
        igdb_game_cover = get_game_cover_art(game_id)

        game = Game(
            name=igdb_game_data['name'],
            artwork=json.dumps(igdb_game_artwork),
            summary=igdb_game_data['summary'],
            igdb_id=igdb_game_data['id'],
            cover_art=igdb_game_cover
        )

        db.session.add(game)
        db.session.commit()

    user = User.query.filter_by(username=session['username']).first()
    game = Game.query.filter_by(igdb_id=game_id).first()

    existing_review = Review.query.filter_by(user_id=user.id,
                                             game_id=game.id).first()

    review = Review(
        user_id=user.id,
        game_id=game.id,
        rating=float(request.form.get('review-rating')),
        heading=request.form.get('review-heading'),
        liked_text=request.form.get('liked-text'),
        disliked_text=request.form.get('disliked-text'),
        hours=int(request.form.get('review-hours')),
    )

    if existing_review:
        print(request)
        flash('You have already created a review for this game')
        return redirect(url_for('manage'))

    db.session.add(review)
    db.session.commit()

    flash('Review added successfully')
    return redirect(url_for('home'))
