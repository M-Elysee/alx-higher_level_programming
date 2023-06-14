#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    delete_list = []
    for key, val in a_dictionary.items():
        if val == value:
            delete_list.append(key)
    for x in delete_list:
        del a_dictionary[x]
    return a_dictionary
