#!/usr/bin/python3
""" *Square #1* """
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """ a class that inherits from Rectangle """
    def __init__(self, size):
        """ Square class initialisation """
        super().integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """ calculates the area of the square """
        return self.__size ** 2
