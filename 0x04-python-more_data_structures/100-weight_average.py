#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    sums = 0
    denom = 0
    for x, y in my_list:
        sums = sums + (x * y)
        denom = denom + y
    return sums / denom
