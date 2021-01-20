#!/usr/bin/python3
"""

function to open and read a file with encoding

"""


def write_file(filename="", text=""):
    """
    reads a file 'with' statement
    returns number of characters written
    """
    with open(filename, 'w') as f:
        return f.write(text)
