#!/usr/bin/python3
"""read_file(filename="")

This module has one function that
reads a file and prints it to standard
output.

"""


def read_file(filename=""):
    """
    Prints a file to standard output
    """
    with open(filename, mode='r+', encoding='utf-8') as a_file:
        print(a_file.read(), end="")
