#!/usr/bin/python3
""" importing json """
import json
"""

writes object to a text file

"""


def save_to_json_file(my_obj, filename):
    """
    writes an object to a text file
    """
    with open(filename, 'w') as f:
        json.dump(my_obj, f)
