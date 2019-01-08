#!/usr/bin/python3
"""print_square(size)

One function that prints a square using the given size
"""


def print_square(size):
    """
    Prints a # square of size size
    """
    if not isinstance(size, int):
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')
    for row in range(size):
        print('#' * size)
