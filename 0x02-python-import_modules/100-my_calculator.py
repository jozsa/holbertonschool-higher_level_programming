#!/usr/bin/python3
from sys import argv
from calculator_1 import add, sub, mul, div
if __name__ == "__main__":
    operator = ['+', '-', '*', '/']
    if len(argv) != 4:
        print('Usage: ./100-my_calculator.py <a> <operator> <b>')
        exit(1)
    a = int(argv[1])
    b = int(argv[3])
    for i, name in enumerate(operator):
        if argv[2][0] == name:
            if name == '+':
                result = add(a, b)
            elif name == '-':
                result = sub(a, b)
            elif name == '*':
                result = mul(a, b)
            elif name == '/':
                result = div(a, b)
            print('{} {} {} = {}'.format(a, name, b, result))
            exit(0)
    print('Unknown operator. Available operators: +, -, * and /')
    exit(1)
