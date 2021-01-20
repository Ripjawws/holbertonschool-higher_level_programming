#!/usr/bin/python3
"""

Creating class student

"""


class Student:
    """
    student class creation
    """
    def __init__(self, first_name, last_name, age):
        """
        initializing students data
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        return in dictionary form
        """
        return(self.__dict__)
