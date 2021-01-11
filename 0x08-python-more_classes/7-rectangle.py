#!/usr/bin/python3
"""

Class Rectangle: create a rectangle

"""


class Rectangle:
    """
    creates a rectangle
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):

        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int and type(value) is not float:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int and type(value) is not float:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """
        defines area of rectangle
        """
        return (self.__width * self.__height)

    def perimeter(self):
        """
        defines perimeter of rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return ((self.__width + self.__height) * 2)

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
                    result = result + str(self.print_symbol)
                result = result + '\n'
            result = result[:-1]
            return result

    def __repr__(self):
        """
        prints visual representation
        """
        return "Rectangle(" + str(self.width) + "," + str(self.height) + ")"

    def __del__(self):
        """
        deletes instances of triangle
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
