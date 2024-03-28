#!/usr/bin/python3

"""
This module fetches the value of the variable X-Request-Id 
from the response header using requests package.
"""

import requests
import sys


def fetch_request_id(url):
    """
    Fetches the value of the variable X-Request-Id from the response header.

    Args:
        url (str): The URL to send the request to.

    Returns:
        None
    """
    response = requests.get(url)
    request_id = response.headers.get('X-Request-Id')
    print(request_id)


if __name__ == "__main__":
    fetch_request_id(sys.argv[1])
