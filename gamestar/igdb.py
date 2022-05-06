"""
IGDB API - https://api-docs.igdb.com/
"""
import os
import requests
from gamestar.twitchapi import get_access_token


def api_request(url_param, body):
    """
    Send the request to the IGDB API

    :param url: The endpoint to which the query relates
    :type url: str
    :param body: The query to be processed
    :type body: str
    :return The Request response
    :rtype Json
    """

    url = f'https://api.igdb.com/v4/{url_param}'
    access_token = get_access_token()
    headers = {
        'Client-ID': os.environ.get('CLIENT_ID'),
        'Authorization': f'{access_token[1]} {access_token[0]}'
    }

    response = requests.post(url, headers=headers, data=body)
    return response.json()


def test():
    """
    Testing API
    """
    url_param = 'games'
    body = 'search "Elden Ring"; fields name, cover, summary; '\
        'where version_parent = null; limit 10;'
    print('|-----------------------------------------------------|')
    print(api_request(url_param, body))
    print('|-----------------------------------------------------|')


test()
