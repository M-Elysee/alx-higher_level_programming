#!/usr/bin/python3
"""*Access and update private attribute*"""


class Square:
    """*a class Square that defines a square*"""
    def __init__(self, size=0):
        """*instatiate a Private instance attribute: size*"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    @property
    def size(self):
        """* retrieve the size*"""
        return self.__size

    @size.setter
    def size(self, value):
        """* sets the size*"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """* returns the current square area*"""
        return self.__size ** 2
