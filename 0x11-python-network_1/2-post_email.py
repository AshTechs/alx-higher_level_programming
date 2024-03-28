#!/usr/bin/python3

"""
Sends a POST request to a given URL with email parameter using urllib package
"""

import urllib.request
import urllib.parse
import sys


def send_post_request(url, email):
    """
    Sends a POST request to the given URL with the email as a parameter.

    Args:
        url (str): The URL to send the POST request to.
        email (str): The email to include as a parameter in the request.

    Returns:
        None
    """
    try:
        data = urllib.parse.urlencode({'email': email}).encode('utf-8')
        req = urllib.request.Request(url, data=data, method='POST')
        with urllib.request.urlopen(req) as response:
            print(response.read().decode('utf-8'))
    except urllib.error.URLError as e:
        print(e.reason)


if __name__ == "__main__":
    send_post_request(sys.argv[1], sys.argv[2])
