#!/usr/bin/python3
"""add_integer(a, b)

This module adds two arguments given to add_integer and returns the sum.

"""


def add_integer(a, b=98):
    """
    Returns the sum of two integers. 2nd argument is set to 98 by default.
    """
    if not isinstance(a, (float, int)):
        raise TypeError('a must be an integer')
    if not isinstance(b, (float, int)):
        raise TypeError('b must be an integer')
    return int(a) + int(b)
