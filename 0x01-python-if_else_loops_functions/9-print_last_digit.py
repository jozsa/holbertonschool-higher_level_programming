#!/usr/bin/python3
def print_last_digit(number):
    lastdigit = abs(number) % 10
    print('{:d}'.format(lastdigit), end="")
    return lastdigit
