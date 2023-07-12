#!/usr/bin/python3
""" *Full rectangle* """
BaseGeometry = __import__('7-base_geometry'). BaseGeometry


class Rectangle(BaseGeometry):
    """ a class that  inherits from BaseGeometry """
    def __init__(self, width, height):
        """ initialise the Rectangle class """
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """ implements the area method """
        return self.__height * self.__width

    def __str__(self):
        """ prints the discription of the class """
        return "[{}] {}/{}".format("Rectangle", self.__width, self.__height)
