#!/usr/bin/python3
""" a Python script that takes in a URL, sends a request to the
    URL and displays the body of the response (decoded in utf-8)
"""
from urllib import request, error
import sys

if __name__ == "__main__":
    try:
        with request.urlopen(sys.argv[1]) as res:
            print(res.read().decode("utf-8"))
    except error.HTTPError as e:
        print("Error code: {}".format(e.code))
