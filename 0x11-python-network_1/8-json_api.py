#!/usr/bin/python3
""" Posting an email """
import requests
from sys import argv


if __name__ == "__main__":

    if (len(argv) > 1):
        letter = argv[1]
    else:
        letter = ""

    data = {'q': letter}
    r = requests.post('http://0.0.0.0:5000/search_user', data=data)
    try:
        body = r.json()
        if (len(body) != 0):
            print("[{}] {}".format(body['id'], body['name']))
        else:
            print("No result")
    except:
        print("Not a valid JSON")
