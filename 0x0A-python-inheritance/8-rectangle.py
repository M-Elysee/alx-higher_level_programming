#!/usr/bin/python3
""" *Rectangle* """
BaseGeometry = __import__('7-base_geometry'). BaseGeometry


class Rectangle(BaseGeometry):
    """ a class that  inherits from BaseGeometry """
    def __init__(self, width, height):
        """ initialise the Rectangle class """
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height
