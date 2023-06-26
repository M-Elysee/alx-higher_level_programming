#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    """ my Print and count integers function """
    leng = 0
    for j in range(x):
        try:
            print("{:d}".format(my_list[j]), end="")
            leng += 1
        except TypeError:
            continue
        except ValueError:
            continue
    print("")
    return leng
