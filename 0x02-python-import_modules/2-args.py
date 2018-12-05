#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    print('{} argument'.format(len(argv) - 1), end="")
    if len(argv) == 1:
        print('s.')
    if len(argv) > 1:
        if len(argv) > 2:
            print('s', end="")
        print(':')
        for i, name in enumerate(argv[1:], start=0):
            print('{}: {}'.format(i + 1, name))
