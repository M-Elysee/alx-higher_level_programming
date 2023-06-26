#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    """ my safe list printing function """
    num = 0
    for j in range(x):
        try:
            print("{}".format(my_list[j]), end="")
            num += 1
        except IndexError:
            break
    print()
    return num
