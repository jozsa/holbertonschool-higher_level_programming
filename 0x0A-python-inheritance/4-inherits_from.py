#!/usr/bin/python3
"""inherits_from(obj, a_class)

Tests whether an object is an
instance inherited from a class

"""


def inherits_from(obj, a_class):
    """
    Returns true if obj is an instance
    inherited from a_class. Otherwise,
    False is returned.
    """
    if not type(obj) is a_class and issubclass(type(obj), a_class):
        return True
    return False
