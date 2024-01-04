#!/usr/bin/python3
from sys import argv
from calculator_1 import add, sub, mul, div
if __name__ == "__main__":
    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    else:
        a = int(argv[2])
        b = int(argv[4])
        if argv[3] == '+':
            print("{}".format(add(a,b)))
        elif argv[3] == '-':
            print("{}".format(sub(a,b)))
        elif argv[3] == '*':
            print("{}".format(mul(a,b)))
        elif argv[3] == '/':
            print("{}".format(add(a,b)))
        else:
