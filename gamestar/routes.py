"""Application Routes"""

import re
import random
import json
from datetime import datetime
from flask import (render_template, request, redirect, url_for, flash,
                   session, jsonify)
from werkzeug.security import generate_password_hash, check_password_hash
from gamestar.igdb import (get_game_data_by_string, get_game_cover_art,
                           get_game_data_by_id, get_game_artwork)
from gamestar import app, db
from gamestar.models import User, Game, Review


@app.route('/', defaults={"page": 1})
@app.route('/<int:page>')
def home(page):
    """
    Render home.html template.
    """
    per_page = 24
    games = Game.query.paginate(page, per_page, error_out=True)

    for game in games.items:

        reviews = Review.query.filter_by(game_id=game.id).all()

        if len(reviews) == 0:
            games = None
            break

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
                      Please Try Again!', 'error')
            return render_template('register.html')

        if re.search('[^A-z0-9]', username):
            flash('Registration Failed:\
                 Username must only contain letters and numbers.\
                      Please Try Again!', 'error')
            return render_template('register.html')

        if password != password_confirm:
            flash('Registration Failed:\
                 Passwords do not match.\
                      Please Try Again!', 'error')
            return render_template('register.html')

        existing_user = User.query.filter_by(username=username).first()

        if existing_user:
            flash('Registration Failed:\
                 Username taken.\
                      Please Try Again!', 'error')
            return render_template('register.html')

        password_hash = generate_password_hash(password)

        user = User(
            username=username, password=password_hash
            )

        db.session.add(user)
        db.session.commit()

        session['username'] = user.username
        flash('Successfully Registered & Logged In!', 'success')
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
                 Username/Password combination not recognized.\
                      Please Try Again!', 'error')
            return redirect(url_for('login'))

        if not check_password_hash(existing_user.password, password):
            flash('Log In Failed:\
                 Username/Password combination not recognized.\
                      Please Try Again!', 'error')
            return redirect(url_for('login'))

        session['username'] = existing_user.username
        flash('Successfully Logged In', 'success')
        return redirect(url_for('home'))

    if 'username' in session:
        flash('You are already logged in.', 'error')
        return redirect(url_for('home'))
    return render_template('login.html', title='Login')


@app.route('/logout')
def logout():
    """
    Logs user out by clearing the session cookie.
    """
    if user_logged_in():
        session.clear()
        flash('Successfully Logged Out', 'success')

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
                      Please Try Again!', 'error')
            return redirect(url_for('profile'))

        existing_user = User.query.filter_by(
            username=session['username']).first()

        if not existing_user:
            flash('Password Change Failed:\
                 Username not found.\
                      Please Try Again!', 'error')
            return redirect(url_for('profile'))

        passwords_match = check_password_hash(
            existing_user.password, current_password)

        if not passwords_match:
            flash('Password Change Failed:\
                 Current Password incorrect.\
                      Please Try Again!', 'error')
            return redirect(url_for('profile'))

        existing_user.password = generate_password_hash(password)

        db.session.commit()
        flash('Password Changed Successfully', 'success')
        return redirect(url_for('profile'))

    # GET Request
    if not user_logged_in():
        flash('You must log in to view this page', 'error')
        return redirect(url_for('login'))

    return render_template('profile.html', user=session['username'],
                           title='Your Profile')


@app.route('/profile/delete', methods=['GET', 'POST'])
def delete_user():
    """Delete user profile, and remove all user data"""

    # POST Request
    if request.method == 'POST':
        username = request.form.get('username')

        if username == 'admin':
            flash('User: Admin, Can not be deleted', 'error')
            return redirect(url_for('profile'))

        if session['username'] != 'admin' and username != session['username']:
            flash('Error deleting profile, '
                  'please contact an administrator', 'error')
            return redirect(url_for('profile'))

        user = User.query.filter_by(username=username).first()
        users_reviews = Review.query.filter_by(user_id=user.id).all()

        for review in users_reviews:
            game = Game.query.filter_by(id=review.game_id).first()

            db.session.delete(review)
            db.session.commit()

            reviews = Review.query.filter_by(game_id=game.id).all()

            if not reviews:
                db.session.delete(game)
                db.session.commit()

        db.session.delete(user)
        db.session.commit()

        if session['username'] == 'admin':
            flash(f'{user.username.capitalize()} '
                  'profile successfully deleted!', 'success')
            return redirect(url_for('user_manager'))

        session.clear()
        flash('User profile successfully deleted!', 'success')
        return redirect(url_for('home'))

    # GET Request
        if not user_logged_in():
            flash('You must log in to view this page', 'error')
            return redirect(url_for('login'))

        return redirect(url_for('profile'))


@app.route('/user_manager')
def user_manager():
    """
    GET: Displays list of registered users
    """
    if not user_logged_in():
        flash('You must log in to view this page', 'error')
        return redirect(url_for('login'))

    if session['username'] != 'admin':
        flash('You are not authorized to access this page', 'error')
        return redirect(url_for('home'))

    users = User.query.all()

    return render_template('user_manager.html',
                           title='User Manager',
                           users=users)


@app.route('/manage', methods=['GET', 'POST'])
def manage():
    """
    GET: Renders manage.html template.
    Displaying reviews user has created if any.
    """

    if user_logged_in():
        user = User.query.filter_by(username=session['username']).first()
        reviews = Review.query.filter_by(user_id=user.id).all()
        user_reviews = []
        for review in reviews:
            game = Game.query.filter_by(id=review.game_id).first()
            user_reviews.append({'game': game, 'review': review})

        return render_template('manage.html', user_reviews=user_reviews,
                               title='Your Reviews')

    flash('You must log in to view this page', 'error')
    return redirect(url_for('login'))


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

            game['anchor_href'] = url_for('add_review', game_id=game['id'])

        return jsonify(data)

    # GET:
    if not user_logged_in():
        flash('You must log in to view this page', 'error')
        return redirect(url_for('login'))

    return render_template('search.html', title='Search Games')


@app.route('/add_review/<game_id>', methods=['GET'])
def add_review(game_id):
    """
    GET: Search IGDB for game by ID, return and render result
    """
    if user_logged_in():

        game = get_game_data_by_id(game_id)[0]

        if 'cover' in game:
            game['cover'] = get_game_cover_art(game_id)
        else:
            game['cover'] = url_for('static',
                                    filename='images/no_cover.webp')

        game['artworks'] = get_game_artwork(game_id)

        if len(game['artworks']) > 0:
            background = random.choice(game['artworks'])
            return render_template('add_review.html',
                                   data=game,
                                   background=background,
                                   title='Create Review')

        return render_template('add_review.html',
                               data=game,
                               title='Create Review')

    flash('You must log in to view this page', 'error')
    return redirect(url_for('login'))


@app.route('/submit_review/<game_id>', methods=['POST'])
def submit_review(game_id):
    """
    Adds users review to database.
    """
    validation_error = False

    review_rating = request.form.get('review-rating').strip()
    review_heading = request.form.get('review-heading').strip()
    review_liked = request.form.get('liked-text').strip()
    review_disliked = request.form.get('disliked-text').strip()
    review_hours = request.form.get('review-hours').strip()

    if len(review_heading) < 10 or len(review_heading) > 65:
        validation_error = True
        flash('Review Heading does not match required length!', 'error')

    if len(review_liked) < 30 or len(review_liked) > 2500:
        flash('Review Liked does not match required length!', 'error')

    if len(review_disliked) < 30 or len(review_disliked) > 2500:
        validation_error = True
        flash('Review Disliked does not match required length!', 'error')

    if len(review_hours) < 1 or len(review_hours) > 5:
        validation_error = True
        flash('Review Hours does not match required length!', 'error')

    if validation_error:
        return redirect(url_for('add_review',
                                game_id=game_id,
                                review_rating=review_rating,
                                review_heading=review_heading,
                                review_liked=review_liked,
                                review_disliked=review_disliked,
                                review_hours=review_hours
                                ))

    if user_logged_in():

        existing_game = Game.query.filter_by(igdb_id=game_id).first()

        if not existing_game:
            igdb_game_data = get_game_data_by_id(game_id)[0]
            igdb_game_artwork = get_game_artwork(game_id)
            igdb_game_cover = get_game_cover_art(game_id)

            if igdb_game_cover is None:
                igdb_game_cover = url_for('static',
                                          filename='images/no_cover.webp')

            if 'summary' not in igdb_game_data:
                igdb_game_data['summary'] = ''

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
            rating=float(review_rating),
            heading=review_heading,
            liked_text=review_liked,
            disliked_text=review_disliked,
            hours=int(review_hours),
            likes='[]'
        )

        if existing_review:
            flash('You have already created a review for this game', 'error')
            return redirect(url_for('manage'))

        db.session.add(review)
        db.session.commit()

        flash('Review added successfully', 'success')
        return redirect(url_for('home'))

    flash('You must log in to view this page', 'error')
    return redirect(url_for('login'))


@app.route('/edit_review/<int:review_id>', methods=['GET', 'POST'])
def edit_review(review_id):
    """
    Renders edit_review.html template.
    POST: Updates users review with new review data.
    """

    review = Review.query.filter_by(id=review_id).first()

    if not review:
        flash('Review Not Found!', 'error')
        return redirect(url_for('home'))

    if not user_logged_in():
        flash('You must be logged in to edit a review', 'error')
        return redirect(url_for('login'))

    game = Game.query.filter_by(id=review.game_id).first()
    user = User.query.filter_by(id=review.user_id).first()

    if session['username'] != 'admin' and user.username != session['username']:
        flash('You can only edit your own reviews', 'error')
        return redirect(url_for('home'))

    if request.method == 'POST':

        review.heading = request.form.get('review-heading')
        review.rating = request.form.get('review-rating')
        review.liked_text = request.form.get('liked-text')
        review.disliked_text = request.form.get('disliked-text')
        review.hours = request.form.get('review-hours')

        db.session.commit()

        return redirect(url_for('game', game_id=game.id))

    if len(json.loads(game.artwork)) > 0:
        background = random.choice(json.loads(game.artwork))
    else:
        background = None

    return render_template('edit_review.html',
                           title='Edit Review',
                           game=game,
                           review=review,
                           background=background)


@app.route('/delete_review/<int:review_id>')
def delete_review(review_id):
    """Delete review stored in database"""
    review = Review.query.filter_by(id=review_id).first()
    user = User.query.filter_by(id=review.user_id).first()

    if session['username'] != 'admin' and user.username != session['username']:
        flash('You can only delete your own reviews', 'error')
        return redirect(url_for('home'))

    db.session.delete(review)
    db.session.commit()

    game = Game.query.get_or_404(review.game_id)

    reviews = Review.query.filter_by(game_id=game.id).all()

    if not reviews:
        db.session.delete(game)
        db.session.commit()

    flash('Review has be deleted successfully.', 'success')
    return redirect(url_for('home'))


@app.route('/review_manager')
def review_manager():
    """
    Displays all reviews if user is admin
    """

    if not user_logged_in():
        flash('You must log in to view this page', 'error')
        return redirect(url_for('login'))

    if session['username'] != 'admin':
        flash('You are not authorized to view this page', 'error')
        return redirect(url_for('home'))

    reviews = Review.query.all()

    for review in reviews:
        username = User.query.filter_by(id=review.user_id).first().username
        game = Game.query.filter_by(id=review.game_id).first()

        review.username = username
        review.game = game

    return render_template('review_manager.html',
                           title='Review Manager',
                           reviews=reviews)


@app.route('/user_reviews/<username>')
def user_reviews(username):
    """
    Displays all reviews by a given user
    """

    user = User.query.filter_by(username=username).first()
    reviews = Review.query.filter_by(user_id=user.id).all()

    for review in reviews:
        game = Game.query.filter_by(id=review.game_id).first()
        review.game = game
        review.likes = json.loads(review.likes)

    return render_template('user_reviews.html',
                           title='Review Manager',
                           reviews=reviews,
                           user=user)


@app.route('/game/<int:game_id>')
def game(game_id):
    """Render users reviews for selected game"""
    if user_logged_in():
        user = User.query.filter_by(username=session['username']).first()
    else:
        user = None

    reviews_data = Review.query.filter_by(game_id=game_id).all()

    total_rating = 0
    for review in reviews_data:
        review.username = User.query.filter_by(
            id=review.user_id).first().username

        review.created_date = datetime.fromtimestamp(
            review.timestamp).strftime('%B %d, %Y')

        review.likes = json.loads(review.likes)

        total_rating += review.rating

    game_data = Game.query.filter_by(id=game_id).first()

    average_rating = total_rating / len(reviews_data)
    game_data.average_rating = average_rating

    if len(json.loads(game_data.artwork)) > 0:
        background = random.choice(json.loads(game_data.artwork))
    else:
        background = None

    return render_template('game.html',
                           title=game_data.name,
                           user=user,
                           game=game_data,
                           reviews=reviews_data,
                           background=background)


@app.route('/likes', methods=['POST'])
def likes():
    """Like button pressed, toggles user ID in games liked list"""
    user_id = User.query.filter_by(username=session['username']).first().id
    review = Review.query.get_or_404(request.form['review_id'])
    likes = json.loads(review.likes)
    if user_id in likes:
        likes.remove(user_id)
    else:
        likes.append(user_id)

    review.likes = json.dumps(likes)

    db.session.add(review)
    db.session.commit()

    return f"{len(likes)}"


@app.errorhandler(404)
def page_not_found(e):
    """Custom 404 Page Not Found"""
    return render_template('404.html', title='404 - Page Not Found'), 404


def user_logged_in():
    """
    Checks if user is logged in.
    If user is not logged in direct user to login screen
    """
    try:
        if session['username']:
            return True
    except:  # noqa
        return False
