#!/usr/bin/python3

"""
This module sends a POST request to http://0.0.0.0:5000/search_user with a letter as a parameter.
"""

import requests
import sys


def search_user(letter):
    """
    Sends a POST request to http://0.0.0.0:5000/search_user with the letter as a parameter.

    Args:
        letter (str): The letter to search for.

    Returns:
        None
    """
    url = "http://0.0.0.0:5000/search_user"
    payload = {'q': letter}
    response = requests.post(url, data=payload)
    try:
        data = response.json()
        if data:
            print("[{}] {}".format(data['id'], data['name']))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")


if __name__ == "__main__":
    letter = sys.argv[1] if len(sys.argv) > 1 else ""
    search_user(letter)
