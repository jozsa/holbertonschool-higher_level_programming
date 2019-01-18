#!/usr/bin/python3
"""to_json_string(my_obj)

One function: returns the JSON representation of an object
"""
import json


def to_json_string(my_obj):
    """
    Returns the JSON representation of my_obj
    """
    return json.dumps(my_obj)
