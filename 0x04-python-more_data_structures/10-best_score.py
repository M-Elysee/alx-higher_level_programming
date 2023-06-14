#!/usr/bin/python3
def best_score(a_dictionary):
    big = None, float("-inf")
    if not a_dictionary:
        return None
    for key, value in a_dictionary.items():
        if isinstance(value, int) and value >= big[1]:
            big = key, value
    return big[0]
