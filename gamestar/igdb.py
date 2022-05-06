"""
IGDB API - https://api-docs.igdb.com/
"""
import os
import requests
from gamestar.twitchapi import get_access_token


def api_request(url_param, body):
    """
    Send the request to the IGDB API.

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


def get_game_data_by_string(query):
    """
    Send the request to the IGDB API using 'games' as 
    the endpoint for the API.

    :param query: The name of the game
    :type query: str
    :return The Request response
    :rtype Json
    """
    body = f'search "{query}"; fields name, cover, summary; '\
        'where version_parent = null; limit 10;'

    return api_request('games', body)


# Test get_game_data_by_string
print(get_game_data_by_string('elden ring'))
