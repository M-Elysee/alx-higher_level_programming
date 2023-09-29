#!/usr/bin/python3
"""a script that list 10 commits (from the most recent to oldest) """
import requests
import sys

if __name__ == "__main__":
    url = "http://api.github.com/repos/{}/{}/commits"\
          .format(sys.argv[2], sys.argv[1])
    res = requests.get(url)
    res = res.json()
    try:
        j = 0
        while (j < 10):
            print("{}: {}".format(res[j].get("sha"),
                  res[j].get("commit").get("author").get("name")))
            j = j + 1
    except IndexError:
        pass
