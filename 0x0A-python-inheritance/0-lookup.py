#!/usr/bin/python3
"""

Function that returns the list of available attributes

"""


def lookup(obj):
    """
    returns a list
    """
    return list(dir(obj))
