#!/usr/bin/python3
from sys import argv
total = 0
if __name__ == "__main__":
    for i, name in enumerate(argv[1:]):
        total += int(name)
    print('{}'.format(total))
