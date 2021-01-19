#!/usr/bin/python3
"""

Checks if is a instance from inherited class

"""


def inherits_from(obj, a_class):
    """checks for inheritance"""
    if type(obj) is a_class:
        return False
    return issubclass(type(obj), a_class)
