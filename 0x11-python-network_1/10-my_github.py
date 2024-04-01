#!/usr/bin/python3

"""
Takes GitHub credentials and displays the user's id using the GitHub API
"""

import requests
import sys

def get_github_user_id(username, password):
    # API endpoint to get user information
    url = 'https://api.github.com/user'

    # Basic authentication using personal access token
    response = requests.get(url, auth=(username, password))
    
    if response.status_code == 200:
        user_id = response.json().get('id')
        print(f"User ID: {user_id}")
    else:
        print("Failed to retrieve user ID. Check your credentials.")

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    
    get_github_user_id(username, password)
