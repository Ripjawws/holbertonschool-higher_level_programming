#!/usr/bin/python3
"""importing rectangle"""
from .rectangle import Rectangle
"""

Inheriting Rectangle for new class Square

"""


class Square(Rectangle):
    """ class Square """
    def __init__(self, size, x=0, y=0, id=None):
        """
        initializes data
        """
        self.size = size
        super().__init__(self.__size, self.__size, x, y, id)

    @property
    def size(self):
        """
        returning size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        setting size
        """
        if (type(value) is not int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__size = value

    def __str__(self):
        """override str"""
        return ("[Square] ({}) {}/{} - {}".format(self.id,
                self.x, self.y, self.__size))

    def update(self, *args, **kwargs):
        """ update arguments """
        attributes = ["id", "size", "x", "y"]
        if args and len(args) != 0:
            for arg in range(len(args)):
                if arg == 0:
                    super().update(args[arg])

                elif arg < len(attributes):
                    setattr(self, attributes[arg], args[arg])
        else:
            for key, value in kwargs.items():
                if key == 'id':
                    super().update(value)
                else:
                    setattr(self, key, value)

    def to_dictionary(self):
        """ returns a dictionary of a class """
        dic = {'id': self.id,
               'size': self.__size,
               'x': self.x,
               'y': self.y
               }
        return dic
