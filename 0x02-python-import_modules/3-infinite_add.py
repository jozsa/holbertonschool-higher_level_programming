#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    total = 0
    for i, name in enumerate(argv[1:]):
        total += int(name)
    print('{}'.format(total))
