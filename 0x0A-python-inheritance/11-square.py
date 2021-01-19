#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle
"""

inherits from rectangle

"""


class Square(Rectangle):
    """
    creates class square and inherits from rectangle
    """
    def __init__(self, size):
        """
        obtaining size and validating int
        """
        self.__size = size
        self.integer_validator("size", size)
        super().__init__(self.__size, self.__size)

    def area(self):
        """
        returns area of square
        """
        return (self.__size ** 2)

    def __str__(self):
        """
        turn obj to str
        """
        return "[Square] {}/{}".format(self.__size, self.__size)
