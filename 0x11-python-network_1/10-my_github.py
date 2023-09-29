#!/usr/bin/python3
""" *a Python script that takes your GitHub credentials
    (username and password) and uses the GitHub API
    to display your id**
"""
import requests
import sys
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    auths = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    res = requests.get("https://api.github.com/user", auth=auths)
    print(res.json().get("id"))
