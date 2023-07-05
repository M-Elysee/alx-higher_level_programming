#!/usr/bin/python3
"""**Compare rectangles**"""


class Rectangle():
    """ **defining the rectangle**"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """ instatiation of it's properties """
        if type(width) is not int:
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = width
        if type(height) is not int:
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """ width getter """
        return self.__width

    @width.setter
    def width(self, value):
        """ width setter """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """ height getter """
        return self.__height

    @height.setter
    def height(self, value):
        """ height setter """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """ returns the area of the rectangle """
        return self.__height * self.__width

    def perimeter(self):
        """ returns the perimeter of the rectangle """
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (self.__width + self.__height) * 2

    def __str__(self):
        """ using str to print the rectangle with # """
        lst = []
        if self.perimeter == 0:
            return ""
        else:
            for i in range(self.__height):
                for j in range(self.__width):
                    lst.append(str(self.print_symbol))
                if i != self.height - 1:
                    lst.append("\n")
        return ''.join(lst)

    def __repr__(self):
        """ returns an official string represantation of the new instance """
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """ function to be called when deleting an instance """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ provide the bigger rectangle """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        return rect_1 if rect_1.area() >= rect_2.area() else rect_2
