#!/usr/bin/python3
"""append_write(filename="", text="")

One function that appends a string to a text file.

"""


def append_write(filename="", text=""):
    """
    Appends text to filename and returns the
    number of characters appended.
    """
    with open(filename, mode='a', encoding='utf-8') as a_file:
        a_file.write(text)
    return len(text)
