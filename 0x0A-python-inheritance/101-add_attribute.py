#!/usr/bin/python3
"""add_attribute(a_class, new_attr, value)

Adds a new attribute to an object if possible.

"""


def add_attribute(a_class, new_attr, value):
    """
    If the object has a __dict__, add the new attribute.
    If not, raise TypeError.
    """
    if not hasattr(a_class, '__dict__'):
        raise TypeError('can\'t add new attribute')
    setattr(a_class, new_attr, value)
