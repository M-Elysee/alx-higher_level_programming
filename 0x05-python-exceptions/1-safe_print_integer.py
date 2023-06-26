#!/usr/bin/python3
def safe_print_integer(value):
    """ my Safe printing of an integers list """
    try:
        print("{:d}".format(value))
        return True
    except(ValueError, TypeError):
        return False
