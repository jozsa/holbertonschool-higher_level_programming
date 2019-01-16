#!/usr/bin/python3
"""lookup(obj)

This module returns a list of available
attributes and methods of an object.

"""


def lookup(obj):
    """
    Returns list of attributes and methods of an object
    """
    return dir(obj)
