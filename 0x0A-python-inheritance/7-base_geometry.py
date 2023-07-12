#!/usr/bin/python3
"""* Integer validator*"""


class BaseGeometry:
    def area(self):
        """ raise an exeption"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ *validates a value* """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
