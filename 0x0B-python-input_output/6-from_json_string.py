#!/usr/bin/python3
"""from_json_string(my_str)

One function: convert a JSON string to
a Python object
"""
import json


def from_json_string(my_str):
    """
    Return a Python object represented
    by JSON string
    """
    return json.loads(my_str)
