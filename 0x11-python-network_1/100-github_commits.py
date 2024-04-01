#!/usr/bin/python3

"""
This script lists 10 commits (from most recent to oldest) of a given repositor
"""

import sys
import requests

def list_commits(repo_name, owner_name):
    """
    Lists 10 commits (from the most recent to oldest) of a given repository

    Args:
        repo_name (str): The name of the repository.
        owner_name (str): The owner of the repository.

    Returns:
        None
    """
    url = f"https://api.github.com/repos/{owner_name}/{repo_name}/commits"
    params = {"per_page": 10}
    response = requests.get(url, params=params)
    if response.ok:
        commits = response.json()
        for commit in commits:
            sha = commit['sha']
            author_name = commit['commit']['author']['name']
            print(f"{sha}: {author_name}")
    else:
        print("Error:", response.text)

if __name__ == "__main__":
    repo_name = sys.argv[1]
    owner_name = sys.argv[2]
    list_commits(repo_name, owner_name)
