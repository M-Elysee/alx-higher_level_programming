#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    """ my 4. Divide a list function"""
    div_list = []
    for i in range(0, list_length):
        try:
            div = my_list_1[i] / my_list_2[i]
            div_list.append(div)
        except ZeroDivisionError:
            print("division by 0")
            div_list.append(0)
        except TypeError:
            print("wrong type")
            div_list.append(0)
        except IndexError:
            print("out of range")
            div_list.append(0)
        finally:
            continue
    return div_list
