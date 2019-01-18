#!/usr/bin/python3
"""class_to_json(obj)

Returns the dictionary description for
simple data structure for JSON serialization
of an object.
"""


def class_to_json(obj):
    """
    Returns the dict associated with obj
    """
    return obj.__dict__
