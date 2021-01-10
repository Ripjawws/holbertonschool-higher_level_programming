#!/usr/bin/python3

"""Prints # square
"""


def text_indentation(text):
    """ indented text maker"""
    if type(text) is not str:
        raise TypeError("text must be a string")
    period = text.replace('. ', '.\n\n')
    period1 = period.replace('? ', '?\n\n')
    period2 = period.replace(': ', ':\n\n')
    print(period2, end='')
