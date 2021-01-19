#!/usr/bin/python3
"""

Inherits and prints in ascending ord

"""


class MyList(list):
    """create mylist class"""
    def print_sorted(self):
        """function to print in sorted form"""
        print(sorted(self))
