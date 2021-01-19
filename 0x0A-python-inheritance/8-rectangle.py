#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry
"""
Return true if object is an instance
of a class
"""


class Rectangle(BaseGeometry):
    """ rectangle class """
    def __init__(self, width, height):
        """initalize data """
        self.__width = width
        self.__height = height
        self.integer_validator('width', width)
        self.integer_validator('height', height)
