#!/usr/bin/python3
""" Handling error """
import urllib.parse
import urllib.request
from sys import argv


if __name__ == "__main__":
    url = argv[1]

    req = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(req) as response:
            info = response.read()
            decoded = info.decode('utf-8')
            print(decoded)
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
