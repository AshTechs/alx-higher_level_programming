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
            response_info = {'type': type(content), 'content': content, 'utf8_content': utf8_content}
    except urllib.error.URLError as e:
        response_info = {'error_message': e.reason}
    
    print("Body response:")
    print("\t- type: {}".format(response_info['type'] if 'type' in response_info else 'Unknown'))
    print("\t- content: {}".format(response_info['content'] if 'content' in response_info else 'Unknown'))
    print("\t- utf8 content: {}".format(response_info['utf8_content'] if 'utf8_content' in response_info else 'Unknown'))

    if 'error_message' in response_info:
        print("Error:", response_info['error_message'])

if __name__ == "__main__":
    fetch_status("https://alx-intranet.hbtn.io/status")
