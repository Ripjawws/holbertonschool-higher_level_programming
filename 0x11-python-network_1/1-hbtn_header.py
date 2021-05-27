#!/usr/bin/python3
"""importing"""
import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    req = urllib.request.Request(url)

    with urllib.request.urlopen(req) as response:
        info = response.info()
        print(response.getheader('X-Request-Id'))
