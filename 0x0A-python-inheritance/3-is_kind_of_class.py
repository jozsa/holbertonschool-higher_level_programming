#!/usr/bin/python3
"""is_kind_of_class(obj, a_class)

Tests if obj is an instance of
a_class, or if obj is an instance
of a class that inherited from a_class.

"""


def is_kind_of_class(obj, a_class):
    """
    Returns True if obj is an instance
    of a_class. Otherwise, returns False.
    """
    return(isinstance(obj, a_class))
