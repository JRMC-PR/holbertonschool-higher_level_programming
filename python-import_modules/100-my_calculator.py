#!/usr/bin/python3
if __name__ == "__main__":
    # TODO: import section
    import calculator_1 as calc
    import sys
argc = len(sys.argv)
if argc != 4:
    print("Usage: ./100-my_calculator.py <a> <operator> <b>")
    sys.exit(1)  # ? exit with function fro sys module
if sys.argv[2] not in "+-*/":  # ? if operator is not in string
    print("Unknown operator. Available operators: +, -, * and /")
    sys.exit(1)
    # set variables a and b and convert to int
a = int(sys.argv[1])
b = int(sys.argv[3])
if sys.argv[2] == "+":
    print(f"{a} + {b} = {calc.add(a, b)}")
elif sys.argv[2] == "-":
    print(f"{a} - {b} = {calc.sub(a, b)}")
elif sys.argv[2] == "*":
    print(f"{a} * {b} = {calc.mul(a, b)}")
elif sys.argv[2] == "/":
    print(f"{a} / {b} = {calc.div(a, b)}")
else:
    print("Unknown operator. Available operators: +, -, * and /")
    sys.exit(1)
