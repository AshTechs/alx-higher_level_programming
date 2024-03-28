#!/usr/bin/python3

"""
Retrieves the user ID using GitHub API with Basic Authentication.
"""

import requests
import sys


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
    headers = {"Authorizatio": f"token {password}"
    response = requests.get(url, headers=headers)
    data = response.json()
    print(data['id'])


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    get_github_id(username, password)
