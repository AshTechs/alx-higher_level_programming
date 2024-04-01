#!/usr/bin/python3

"""
This module fetches data from a given URL using requests package.
"""

import requests

def fetch_status_with_requests(url):
    """
    Fetches the status from the given URL using requests package.

    Args:
        url (str): The URL to fetch the status from.

    Returns:
        None
    """
    response = requests.get(url)
    content_type = response.headers.get('Content-Type', 'Unknown')
    content = response.text

    print("Body response:")
    print("\t- type: {}".format(type(content)))
    print("\t- content: {}".format(content))

if __name__ == "__main__":
    fetch_status_with_requests("https://alx-intranet.hbtn.io/status")
