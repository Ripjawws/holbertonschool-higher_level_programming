#!/usr/bin/python3
""" Posting an email """
import requests
from sys import argv


if __name__ == "__main__":

    username = argv[1]
    password = argv[2]

    r = requests.get('https://api.github.com/user', auth=(username, password))
    if (r.status_code >= 400):
        print("None")
    else:
        body = r.json()
        print(body['id'])
