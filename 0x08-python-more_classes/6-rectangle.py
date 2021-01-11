#!/usr/bin/python3

"""
Class Rectangle: creates a rectangle class
"""


class Rectangle:
    """
    Create an empty rectangle class
    """
    number_of_instances = 0
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
        define area of rectangle
        """
        return (self.__width) * (self.__height)

    def perimeter(self):
        """
        define perimeter of rectangle
        """
        return ((self.__width) + (self.__height)) * 2
        if self.width or self.height == 0:
            perimeter == 0

    def __str__(self):
        """
        prints visual representation
        """
        result = ""

        if self.__width == 0 or self.__height == 0:
            return result
        else:
            for i in range(self.__height):
                for j in range(self.__width):
                    result = result + "#"
                result = result + '\n'
            result = result[:-1]
            return result

    def __repr__(self):
        return "Rectangle(" + str(self.width) + "," + str(self.height) + ")"

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
