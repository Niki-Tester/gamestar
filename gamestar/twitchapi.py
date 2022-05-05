"""
The TwitchAPI is used to obtain an access token.
The access token is stored in a mongoDB database.
The access token has an expiry date, and must be
updated before the token expires.
"""
import os
import time
import math
import requests
from gamestar.models import Twitch
from gamestar import db


def new_access_token():
    """
    Makes a post request to the twitch API to
    obtain an access token
    """
    url = 'https://id.twitch.tv/oauth2/token?'\
        f'client_id={os.environ.get("CLIENT_ID")}'\
        f'&client_secret={os.environ.get("CLIENT_SECRET")}'\
        '&grant_type=client_credentials'

    result = requests.post(url)
    data = result.json()

    existing_token = Twitch.query.get(1)

    if existing_token:
        existing_token.access_token = data['access_token']
        existing_token.expires_in = data['expires_in']
        existing_token.token_type = data['token_type']
        existing_token.date_added = math.floor(time.time())

        # pylint: disable = no-member
        db.session.add(existing_token)
        db.session.commit()
    else:
        token = Twitch(
            access_token=data['access_token'],
            expires_in=data['expires_in'],
            token_type=data['token_type'],
            date_added=math.floor(time.time())
        )

        # pylint: disable = no-member
        db.session.add(token)
        db.session.commit()


def get_access_token():
    """
    Checks if current access token has expired,
    if so calls new_access_token and stores the
    new access token in the database.

    If current access token has not expires,
    returns the current access token from database.
    """

    current_token = Twitch.query.get(1)

    current_token_expires = current_token.date_added + current_token.expires_in

    difference = current_token_expires - math.floor(time.time())

    if difference < 86400:  # Less than one day remaining on access_token
        new_access_token()
        token = Twitch.query.get(1)
        return (token.access_token, token.token_type)

    else:
        return (current_token.access_token, current_token.token_type)
