#!/usr/bin/python3

"""
Class Rectangle: creates a rectangle class
"""


class Rectangle:
    """
    Create an empty rectangle class
    """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    def area(self):
        """
        area of rectangle
        """

        return (self.__width) * (self.__height)

    def perimeter(self):
        """
        perimeter of rectangle
        """
        if self.width or self.height == 0:
            return = 0
        return ((self.__width) + (self.__height)) * 2
