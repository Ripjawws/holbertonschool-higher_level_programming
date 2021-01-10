#!/usr/bin/python3

"""Prints name and lastname
"""


def say_my_name(first_name, last_name=""):
    """ function to print strings"""
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    elif type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
