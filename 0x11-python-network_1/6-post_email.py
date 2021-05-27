#!/usr/bin/python3
""" Posting an email """
import requests
from sys import argv


if __name__ == "__main__":
    url = argv[1]
    email = argv[2]
    value = {'email': email}

    r = requests.post(url, data=value)
    print(r.text)
