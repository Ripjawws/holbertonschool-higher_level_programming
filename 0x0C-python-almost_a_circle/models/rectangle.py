#!/usr/bin/python3
"""importing a base"""
from .base import Base
"""

Inheriting base for new class Rectangle

"""


class Rectangle(Base):
    """
    creates class rectangle and inherits Base
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        initializing the data
        """
        Base.__init__(self, id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
        defining width getter
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        setting the value of width
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        """
        defining height getter
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        setting the value of height
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    @property
    def x(self):
        """
        defining x getter
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        setting value for x
        """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        """
        defining x getter
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        setting value for y
        """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        """
        retreives area of rectangle
        """
        return self.height * self.width

    def display(self):
        """
        prints out rectangle in #
        """
        for i in range(self.__y):
            print('' * self.__y)
        for i in range(self.__height):
            print(' ' * self.__x, end='')
            print('#' * self.__width)

    def __str__(self):
        """
        prints out
        """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x, \
            self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """
        assisgns argument to every value
        """
        attributes = ["id", "width", "height", "x", "y"]
        if not args:
            for key, value in kwargs.items():
                setattr(self, key, value)
        else:
            for arg in range(len(args)):
                setattr(self, attributes[arg], args[arg])

    def to_dictionary(self):
        """
        returns a dictionary of class
        """
        dic = {'id': self.id, 'width': self.__width, \
            'height': self.__height, 'x': self.__x, 'y': self.__y}
        return dic
