#!/usr/bin/python3
""" *My list* """


class MyList(list):
    """ *a class that inherits from list* """
    def print_sorted(self):
        """ prints the the object in asscending order """
        print(sorted(self))
