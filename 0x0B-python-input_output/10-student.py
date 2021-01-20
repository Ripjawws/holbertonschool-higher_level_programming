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
    def to_json(self, attrs=None):
        """
        return in dictionary form
        """
        tmp = {}
        if type(attrs) is not list:
            return(self.__dict__)
        else:
            for i in attrs:
                if i in self.__dict__:
                    tmp[i] = self.__dict__[i]
            return tmp
