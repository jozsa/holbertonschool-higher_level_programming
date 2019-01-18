#!/usr/bin/python3
"""class_to_json(obj)

Returns the dictionary description for
simple data structure for JSON serialization
of an object.
"""
import json


def class_to_json(obj):
    """
    Converts class' dict into str then
    returns the dict associated with that str.
    """
    obj_dict_str = json.dumps(obj.__dict__)
    return json.loads(obj_dict_str)
