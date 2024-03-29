#!/usr/bin/python3

"""
This module fetches data from a given URL using urllib package.
"""

import urllib.request
import urllib.error
import sys

url = 'https://alx-intranet.hbtn.io/status'

req = urllib.request.Request(url)
with urllib.request.urlopen(req) as response:
    for line in response:
        print('- {}'.format(line.decode('utf-8').strip()))
