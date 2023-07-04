#!/usr/bin/python3
""" *** Text indentation *** """


def text_indentation(text):
    """prints a text after each of these characters: ., ? and :"""
    if type(text) is not str:
        raise TypeError("text must be a string")
    text_line = []
    for i in text:
        if i not in [".", "?", ":"]:
            text_line.append(i)
        else:
            text_line.append(i)
            text_line = trim(text_line)
            print("{}\n".format(''.join(text_line)))
            text_line = []
    text_line = trim(text_line)
    print("{}".format(''.join(text_line)), end="")


def trim(text_list):
    """ trims the space before a line """
    text_list = list(''.join(text_list).lstrip())
    return text_list
