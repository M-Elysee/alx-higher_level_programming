#!/usr/bin/python3
"""* Coordinates of a square*"""


class Square:
    """*a class Square that defines a square*"""
    def __init__(self, size=0, position=(0, 0)):
        """* initiate size and position*"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
        if (not isinstance(position, tuple) or len(position) != 2 or
            not all(isinstance(i, int) for i in position) or
                not all(i >= 0 for i in position)):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = position

    @property
    def size(self):
        """ gets the size attribute"""
        return self.__size

    @size.setter
    def size(self, value):
        """ sets the size attribute """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """ gets the position attribute """
        return self.__position

    @position.setter
    def position(self, value):
        """ sets the position attribute """
        if (not isinstance(value, tuple) or len(value) != 2 or
            not all(isinstance(i, int) for i in value) or
                not all(i >= 0 for i in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """*returns the current square area*"""
        return self.__size ** 2

    def my_print(self):
        """* prints in stdout the square with the character #*"""
        if self.__size == 0:
            print("")
            return
        else:
            for n in range(self.__position[1]):
                print("")
            for i in range(self.__size):
                for j in range(self.__position[0]):
                    print(" ", end="")
                for k in range(self.__size):
                    print("#", end="")
                print("")
