#!/usr/bin/python3
"""*Printing a square*"""


class Square:
    """*a class Square that defines a square*"""
    def __init__(self, size=0):
        """*initiates a Private instance attribute: size*"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    @property
    def size(self):
        """ gets size attribute """
        return self.__size

    @size.setter
    def size(self, value):
        """ sets size attribute """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """* returns the current square area*"""
        return self.__size ** 2

    def my_print(self):
        """* prints in stdout the square with the character #*"""
        if self.__size == 0:
            print("")
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print()
