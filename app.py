"""
GameStar - A web application for users to find reviews
on video games they would like to play, and leave reviews
on games they have played.
Full readme available at: https://github.com/Niki-Tester/gamestar
"""

import os
from flask import Flask

if os.path.exist('env.py'):
    # flake8: noqa: f401 pylint: disable = unused-import
    import env

app = Flask(__name__)

app.config['MONGO_URI'] = os.environ.get('MONGO_URI')
app.config['MONGO_DBNAME'] = os.environ.get('MONGO_DBNAME')

mongo = Pymongo(app)
