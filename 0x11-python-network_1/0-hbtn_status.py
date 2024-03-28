#!/usr/bin/python3

"""
This module fetches data from a given URL using urllib package.
"""

import urllib.request
import urllib.error
import sys


def fetch_status(url):
    """
    Fetches the status from the given URL using urllib.

    Args:
        url (str): The URL to fetch the status from.

    Returns:
        str: The status fetched from the URL.
    """
    try:
        with urllib.request.urlopen(url) as response:
            status = response.read()
            print("- Body response:")
            print("\t- type: {}".format(type(status)))
            print("\t- content: {}".format(status.decode('utf-8')))
    except urllib.error.URLError as e:
        print(e.reason)


if __name__ == "__main__":
    fetch_status("https://alx-intranet.hbtn.io/status")
