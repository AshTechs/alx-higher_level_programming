#!/usr/bin/python3

"""
Fetches bdy of response frm a gvn URL using requests pckg & handles HTTP errors
"""

import requests
import sys


def fetch_body(url):
    """
    Fetches the body of the response from the given URL.

    Args:
        url (str): The URL to fetch the response body from.

    Returns:
        None
    """
    response = requests.get(url)
    if response.status_code >= 400:
        print("Error code:", response.status_code)
    else:
        print(response.text)


if __name__ == "__main__":
    fetch_body(sys.argv[1])
