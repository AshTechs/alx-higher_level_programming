#!/usr/bin/python3

"""
This script fetches the user ID using GitHub API with Basic Authentication
"""

import sys
import requests

def get_github_user_id(username, token):
    """
    Fetches GitHub user ID for the given username using a personal access token

    Args:
        username (str): GitHub username.
        token (str): Personal access token (password).

    Returns:
        str: GitHub user ID.
    """
    try:
        g = Github(login_or_token=token)
        user = g.get_user(username)
        return user.id
    except Exception as e:
        print(f"Error fetching user ID: {e}")
        return None

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 github_user_id.py <username> <access_token>")
        sys.exit(1)

    username, access_token = sys.argv[1], sys.argv[2]
    user_id = get_github_user_id(username, access_token)

    if user_id:
        print(f"GitHub user ID for {username}: {user_id}")
    else:
        print("Failed to retrieve user ID. Check your credentials.")
