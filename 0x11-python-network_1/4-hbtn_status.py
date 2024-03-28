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
    print("- Body response:")
    print("\t- type: {}".format(type(response.text)))
    print("\t- content: {}".format(response.text))


if __name__ == "__main__":
    fetch_status_with_requests("https://alx-intranet.hbtn.io/status")
