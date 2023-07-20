#!/usr/bin/python3
""" imprimenting a class square """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Class square """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ gets the size of a square instance """
        return self.width

    @size.setter
    def size(self, value):
        """ sets the size of a square instance """
        self.width = value
        self.height = value

    def __str__(self):
        """ returns a represatations of an instance """
        return ("[Square] ({}) {}/{} - {}".format(self.id,
                self.x, self.y, self.width))

    def update(self, *args, **kwargs):
        """ updates the attributes of an instance """
        if not args and kwargs:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)
        if args and len(args) >= 1 and args[0]:
            self.id = args[0]
        if args and len(args) >= 2 and args[1]:
            self.size = args[1]
        if args and len(args) >= 3 and args[2]:
            self.x = args[2]
        if args and len(args) >= 4 and args[3]:
            self.y = args[3]

    def to_dictionary(self):
        """ return a dictionary represantation of a square instance """
        return {"id": self.id, "x": self.x, "size": self.size, "y": self.y}
