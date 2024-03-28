#!/usr/bin/python3

"""
This module retrieves information about a given repository using requests package.
"""

import requests
import sys


def get_repository_info(repo_name, owner_name):
    """
    Retrieves information about a given repository.

    Args:
        repo_name (str): The name of the repository.
        owner_name (str): The name of the repository owner.

    Returns:
        None
    """
    url = f"https://api.github.com/repos/{owner_name}/{repo_name}"
    response = requests.get(url)
    data = response.json()
    print(data)


if __name__ == "__main__":
    repo_name = sys.argv[1]
    owner_name = sys.argv[2]
    get_repository_info(repo_name, owner_name)
