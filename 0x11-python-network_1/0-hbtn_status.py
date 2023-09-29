#!/usr/bin/python3
""" a Python script that fetches and format the responce of a URL """
import urllib.request

if __name__ == "__main__":
    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as res:
        res = res.read()
        print('Body response:')
        print("\t- type: {}".format(res.__class__))
        print("\t- content: {}".format(res))
        print("\t- utf8 content: {}".format(res.decode('utf8')))
