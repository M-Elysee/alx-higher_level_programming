#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    args = sys.argv[1:]
    number = [int(arg) for arg in args]
    s = 0
    for i in number:
        s += i
    print("{}".format(s))
