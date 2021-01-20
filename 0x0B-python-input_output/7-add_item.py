#!/usr/bin/python3
""" importing json and functions """
import json
import os
from sys import argv
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
"""

saves and loads from python to json

"""
if __name__ == "__main__":
    name ="add_item.json"
    if os.path.isfile(name):
        mylist = load_from_json_file(name)
    else:
        mylist = []
    for i in range(1, len(argv)):
        mylist.append(argv[i])
    save_to_json_file(mylist, name)
    