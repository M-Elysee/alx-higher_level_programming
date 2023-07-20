#!/usr/bin/python3
"""*First Rectangle*"""
from models.base import Base


class Rectangle(Base):
    """Class Rectangle inherits from Base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """ initialize the Rectangle class """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """ gets the width """
        return self.__width

    @width.setter
    def width(self, value):
        """ sets the width """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ gets the height """
        return self.__height

    @height.setter
    def height(self, value):
        """ sets the height """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ gets the x variable """
        return self.__x

    @x.setter
    def x(self, value):
        """ sets the x variable """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ gets the y variable """
        return self.__y

    @y.setter
    def y(self, value):
        """ sets the y vaariable """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ returns the area of the rectangle """
        return self.__height * self.__width

    def display(self):
        """that prints in stdout the Rectangle instance with the character #"""
        if self.__width == 0 or self.__height == 0:
            print("")
        else:
            for n in range(self.__y):
                print("")
            for i in range(self.__height):
                for k in range(self.__x):
                    print(" ", end="")
                for j in range(self.__width):
                    print("#", end="")
                print("")

    def __str__(self):
        """ return a represantation of a class"""
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                self.__x, self.__y, self.__width, self.__height))

    def update(self, *args, **kwargs):
        """ assignes arguments to attributes in this class """
        if args and len(args) >= 1 and args[0]:
            self.id = args[0]
        if args and len(args) >= 2 and args[1]:
            self.width = args[1]
        if args and len(args) >= 3 and args[2]:
            self.height = args[2]
        if args and len(args) >= 4 and args[3]:
            self.x = args[3]
        if args and len(args) >= 5 and args[4]:
            self.y = args[4]
        if (not args or len(args) == 0) and kwargs:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)

    def to_dictionary(self):
        """ returns a dictionary represtantion of am instanc"""
        return {"x": self.x, "y": self.y, "id": self.id,
                "height": self.height, "width": self.width}
