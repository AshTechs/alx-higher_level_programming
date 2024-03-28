#!/usr/bin/python3

"""
Fetches the bdy of a respns frm a gvn URL using urllib pckg & hndls HTTP errors
"""

import urllib.request
import urllib.error
import sys


def fetch_body(url):
    """
    Fetches the body of the response from the given URL.

    Args:
        url (str): The URL to fetch the response body from.

    Returns:
        None
    """
    try:
        with urllib.request.urlopen(url) as response:
            print(response.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))


if __name__ == "__main__":
    fetch_body(sys.argv[1])
