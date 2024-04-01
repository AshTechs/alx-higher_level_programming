#!/usr/bin/python3

"""
This script fetches the user ID using GitHub API with Basic Authentication.
"""

import sys
import requests

def get_github_id(username, password):
    """
    Retrieves the user ID using GitHub API with Basic Authentication.

    Args:
        username (str): The GitHub username.
        password (str): The personal access token.

    Returns:
        None
    """
    url = "https://api.github.com/user"
    auth = (username, password)
    response = requests.get(url, auth=auth)
    if response.ok:
        data = response.json()
        print(data['id'])
    else:
        print("Error:", response.text)

if __name__ == "__main__":
    username, password = sys.argv[1:3]
    get_github_id(username, password)
