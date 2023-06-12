#!/usr/bin/python3
def no_c(my_string):
    new_string = [i for i in my_string if i != 'C' and i != 'c']
    return (''.join(new_string))

