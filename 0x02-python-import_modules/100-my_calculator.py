#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys
    args = sys.argv[1:]
    size = len(args)
    operators = ["+", "-", "/", "*"]
    if size != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    if args[1] not in operators:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    else:
        a = int(args[0])
        b = int(args[2])
        if args[1] == "+":
            print("{} + {} = {}".format(a, b, add(a, b)))
        elif args[1] == "-":
            print("{} - {} = {}".format(a, b, sub(a, b)))
        elif args[1] == "*":
            print("{} * {} = {}".format(a, b, mul(a, b)))
        else:
            print("{} / {} = {}".format(a, b, div(a, b)))
