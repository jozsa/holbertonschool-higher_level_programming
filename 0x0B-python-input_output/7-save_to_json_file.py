#!/usr/bin/python3
"""save_to_json_file(my_obj, filename)

One function: write an object to a text file using JSON representation
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Write JSON representation of my_obj to filename
    """
    with open(filename, mode='w+', encoding='utf-8') as a_file:
        json.dump(my_obj, a_file)
