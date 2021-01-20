#!/usr/bin/python3
""" importing json """
import json
"""

writes object to a text file

"""


def load_from_json_file(filename):
    """
    writes an object to a text file
    """
    with open(filename, 'r') as f:
        new = json.load(f)
        return new
