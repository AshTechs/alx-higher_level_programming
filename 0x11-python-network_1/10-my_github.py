#!/usr/bin/python3

"""
Retrieves the user ID using GitHub API with Basic Authentication.
"""

import requests
import sys

username = sys.argv[1]
password = sys.argv[2]

url = 'https://api.github.com/user'

response = requests.get(url, auth=(username, password))
print(response.json()['id'])
