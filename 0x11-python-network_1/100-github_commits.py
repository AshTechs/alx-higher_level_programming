#!/usr/bin/python3

"""
Retrieves information about a given repository using requests package
"""

import requests
import sys

def get_repository_info(repo_name, owner_name):
    """
    Retrieves information about a given repository using GitHub API

    Args:
        repo_name (str): The name of the repository.
        owner_name (str): The name of the repository owner.

    Returns:
        None
    """
    url = f"https://api.github.com/repos/{owner_name}/{repo_name}"
    response = requests.get(url)
    if response.ok:
        data = response.json()
        print(data)
    else:
        print("Error:", response.text)

if __name__ == "__main__":
    repo_name = sys.argv[1]
    owner_name = sys.argv[2]
    get_repository_info(repo_name, owner_name)

