#!/usr/bin/python3
"""write_file(filename="", text="")

One function that writes a string to a text file.

"""


def write_file(filename="", text=""):
    """
    Writes text into filename and returns the
    number of characters written.
    """
    with open(filename, mode='w', encoding='utf-8') as a_file:
        a_file.write(text)
    return len(text)
