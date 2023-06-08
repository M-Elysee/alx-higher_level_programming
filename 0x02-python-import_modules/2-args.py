#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    args = sys.argv[1:]
    length = len(args)
    if length > 1:
        print("{} arguments:".format(length))
    elif length == 1:
        print("{} argument:".format(length))
    else:
        print("{} arguments.".format(length))
    for index, i in enumerate(args):
        print("{}: {}".format(index + 1, i))
