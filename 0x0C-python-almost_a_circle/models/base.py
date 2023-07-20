#!/usr/bin/python3
"""Base class"""
import json
import csv
"""import turtle"""


class Base:
    """ *a class that will be inherited by othes* """
    __nb_objects = 0

    def __init__(self, id=None):
        """ *initialise the id* """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """*returns the JSON string representation of list_dictionaries*"""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """*writes the JSON string representation of list_objs to a file*"""
        filename = cls.__name__ + ".json"
        with open(filename, "w") as jsonfile:
            if list_objs is None:
                jsonfile.write("[]")
            else:
                list_dic = [obj.to_dictionary() for obj in list_objs]
                jsonfile.write(Base.to_json_string(list_dic))

    @staticmethod
    def from_json_string(json_string):
        """*returns the list of the JSON string*"""
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """*returns an instance with all attributes already set*"""
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                new = cls(1, 1)
            else:
                new = cls(1)
            new.update(**dictionary)
            return new

    @classmethod
    def load_from_file(cls):
        """*Return a list of class instance from a file of JSON strings.*"""
        filename = str(cls.__name__) + ".json"
        try:
            with open(filename, "r") as jsonfile:
                list_dic = Base.from_json_string(jsonfile.read())
                return [cls.create(**dic) for dic in list_dic]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """*Write the CSV serialization of a list of objects to a file.*"""
        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline="") as csvfile:
            if list_objs is None or list_objs == []:
                csvfile.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """*Return a list of classes instantiated from a CSV file.*"""
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline="") as csvfile:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(csvfile, fieldnames=fieldnames)
                list_dicts = [dict([key, int(value)]
                              for key, value in dic.items())
                              for dic in list_dicts]
                return [cls.create(**dic) for dic in list_dicts]
        except IOError:
            return []
"""
    @staticmethod
    def draw(list_rectangles, list_squares):
        *Draw Rectangles and Squares using the turtle
        turtes = turtle.Turtle()
        turtes.screen.bgcolor("#b7312c")
        turtes.pensize(3)
        turtes.shape("turtle")

        turtes.color("#ffffff")
        for r in list_rectangles:
            turtes.showturtle()
            turtes.up()
            turtes.goto(r.x, r.y)
            turtes.down()
            for j in range(2):
                turtes.forward(r.width)
                turtes.left(90)
                turtes.forward(r.height)
                turtes.left(90)
            turtes.hideturtle()

        turtes.color("#b5e3d8")
        for s in list_squares:
            turtes.showturtle()
            turtes.up()
            turtes.goto(s.x, s.y)
            turtes.down()
            for j in range(2):
                turtes.forward(s.width)
                turtes.left(90)
                turtes.forward(s.height)
                turtes.left(90)
            turtes.hideturtle()

        turtle.exitonclick()"""
