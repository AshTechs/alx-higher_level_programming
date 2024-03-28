#!/usr/bin/python3

"""
This module fetches the X-Request-Id variable from the header of a response using urllib package.
"""

import urllib.request
import urllib.error
import sys


def fetch_request_id(url):
    """
    Fetches the X-Request-Id variable from the header of a response.

    Args:
        url (str): The URL to send the request to.

    Returns:
        str: The value of the X-Request-Id variable found in the header.
    """
    try:
        with urllib.request.urlopen(url) as response:
            request_id = response.headers.get('X-Request-Id')
            print(request_id)
    except urllib.error.URLError as e:
        print(e.reason)


if __name__ == "__main__":
    fetch_request_id(sys.argv[1])
