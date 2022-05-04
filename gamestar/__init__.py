
"""Gamestar Application Initialization"""
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

if os.path.exists('env.py'):
    import env


app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_URL')

db = SQLAlchemy(app)

# flake8: noqa pylint: disable = wrong-import-position
from gamestar import routes