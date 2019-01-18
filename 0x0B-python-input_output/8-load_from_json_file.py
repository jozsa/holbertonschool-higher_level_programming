#!/usr/bin/python3
"""load_from_json_file(filename)

One function: Create object from JSON file
"""
import json


def load_from_json_file(filename):
    """
    Create object from filename
    """
    with open(filename, encoding='utf-8') as a_file:
        return json.load(a_file)
