#!/usr/bin/python3
def safe_print_division(a, b):
    """ my Integers division with debug function """
    try:
        div = a / b
    except(TypeError, ZeroDivisionError):
        div = None
    finally:
        print("Inside result: {}".format(div))
    return div
