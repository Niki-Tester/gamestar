"""
GameStar - A web application for users to find reviews
on video games they would like to play, and leave reviews
on games they have played.
Full readme available at: https://github.com/Niki-Tester/gamestar
"""

import os
from flask import Flask, render_template, request
from flask_pymongo import PyMongo
from werkzeug.security import generate_password_hash

if os.path.exists('env.py'):
    # flake8: noqa: f401 pylint: disable = unused-import
    import env

app = Flask(__name__)

app.config['MONGO_URI'] = os.environ.get('MONGO_URI')
app.config['MONGO_DBNAME'] = os.environ.get('MONGO_DBNAME')

mongo = PyMongo(app)

@app.route('/')
def index():
    """
    Render home.html template
    """
    return render_template('home.html') 


@app.route('/register', methods=['GET', 'POST'])
def register():
    """
    Render register.html template.
    Get userdata from form if POST method.
    """
    if request.method == 'POST':
        existing_user = mongo.db.users.find_one({'username' : request.form.get('username').lower()})
        if existing_user == None:
            new_user = mongo.db.users.insert_one({
                'username': request.form.get('username').lower(),
                'password' : generate_password_hash(request.form.get('password'))
            })

            return render_template('home.html')            

    return render_template('register.html')


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)