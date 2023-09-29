#!/usr/bin/python3
""" a Python script that takes in a URL and an email, sends a POST
    request to the passed URL with the email as a parameter, and 
    displays the body of the response (decoded in utf-8)
"""
from urllib import request, parse
import sys

if __name__ == "__main__":
    data = parse.urlencode({"email" : sys.argv[2]}).encode("ascii")
    req = request.Request(sys.argv[1], data)
    with request.urlopen(req) as res:
        print(res.read().decode("utf-8"))
