#!/usr/bin/python3

"""
This module sends a POST request to a given URL with an email parameter using requests package.
"""

import requests
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
    payload = {'email': email}
    response = requests.post(url, data=payload)
    print(response.text)


if __name__ == "__main__":
    send_post_request(sys.argv[1], sys.argv[2])
