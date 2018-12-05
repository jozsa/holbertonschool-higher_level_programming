#!/usr/bin/python3
from calculator_1 import add, sub, mul, div  # import calculator functions
if __name__ == "__main__":  # make sure program doesn't execute when imported
    a = 10
    b = 5
    print('{} + {} = {}'.format(a, b, add(a, b)))  # add
    print('{} - {} = {}'.format(a, b, sub(a, b)))  # subtract
    print('{} * {} = {}'.format(a, b, mul(a, b)))  # multiply
    print('{} / {} = {}'.format(a, b, div(a, b)))  # divide
