#!/usr/bin/python3
"""

Returns true if the object is exactly an instance of clase if not False

"""


def is_same_class(obj, a_class):
    """ checks if its an instance, True,False"""
    return type(obj) is a_class
