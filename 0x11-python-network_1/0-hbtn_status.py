#!/usr/bin/python3

"""
This module fetches data from a given URL using urllib package.
"""

import urllib.request
import urllib.error

def fetch_status(url):
    """
    Fetches the status from the given URL using urllib.

    Args:
        url (str): The URL to fetch the status from.

    Returns:
        None
    """
    try:
        with urllib.request.urlopen(url) as response:
            content = response.read()
            utf8_content = content.decode('utf-8')
    except urllib.error.URLError as e:
        print(e.reason)
    else:
        print("Body response:")
        print("\t- type: {}".format(.get(type(content))))
        print("\t- content: {}".format(.get(content)))
        print("\t- utf8 content: {}".format(.get(utf8_content)))

if __name__ == "__main__":
    fetch_status("https://alx-intranet.hbtn.io/status")
