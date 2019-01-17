#!/usr/bin/python3
"""number_of_lines(filename="")

Only one function that counts the
number of lines in a file.

"""


def number_of_lines(filename=""):
    """
    Counts the number of lines in a file
    """
    count = 0
    with open(filename, encoding='utf-8') as a_file:
        for line in a_file:
            count += 1
    return count
