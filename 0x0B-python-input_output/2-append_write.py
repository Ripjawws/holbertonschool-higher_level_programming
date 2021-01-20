#!/usr/bin/python3
"""

function to open and read a file with encoding

"""


def append_write(filename="", text=""):
    """
    appends a string to end of txt file
    returns number of characters added
    """
    with open(filename, 'a') as f:
        return f.write(text)
