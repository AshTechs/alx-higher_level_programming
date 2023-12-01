#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys

    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    operator = sys.argv[2]
    if operator not in ops:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    try:
        x = int(sys.argv[1])
        y = int(sys.argv[3])
    except ValueError:
        print("Both <a> and <b> should be integers")
        sys.exit(1)

    if operator == "/" and y == 0:
        print("Cannot divide by zero")
        sys.exit(1)

    ops = {"+": add, "-": sub, "*": mul, "/": div}
    result = ops[operator](x, y)
    print("{} {} {} = {}".format(x, operator, y, result))
