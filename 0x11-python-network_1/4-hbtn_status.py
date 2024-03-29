#!/usr/bin/python3

"""
This module fetches data from a given URL using requests package.
"""

import requests

url = 'https://alx-intranet.hbtn.io/status'

response = requests.get(url)
for line in response.text.split("\n"):
    print('- {}'.format(line))
