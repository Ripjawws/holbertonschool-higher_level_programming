#!/usr/bin/python3
"""

function to open and read a file with encoding

"""


def read_file(filename=""):
    """
    reads a file 'with' statement
    """
    with open(filename, encoding='utf-8') as f:
        print(f.read(), end="")
