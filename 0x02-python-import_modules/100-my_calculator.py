#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys
    if (len(sys.argv[1:]) != 3):
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    else:
        a = int(sys.argv[1])
        op = sys.argv[2]
        b = int(sys.argv[3])
        if op == "+":
            s = add(a, b)
        elif op == "-":
            s = sub(a, b)
        elif op == "*":
            s = mul(a, b)
        elif op == "/":
            s = div(a, b)
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
        print("{} {} {} = {}".format(a, op, b, s))
