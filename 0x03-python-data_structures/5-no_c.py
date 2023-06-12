#!/usr/bin/python3
def no_c(my_string):
    string_list = list(my_string)
    for i in string_list:
        if i == 'c' or i == 'C':
            string_list.pop(string_list.index(i))
    return (''.join(string_list))
