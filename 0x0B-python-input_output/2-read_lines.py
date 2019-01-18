#!/usr/bin/python3
"""read_lines(filename="", nb_lines=0)

Reads n lines of a text file and prints
it to stdout.
"""


def read_lines(filename="", nb_lines=0):
    """
    Reads a file and prints it up to nb_lines.
    If nb_lines is less than or equal to zero, or
    if nb_lines is more than or equal to the number
    of lines in the file, the whole file is printed.
    """
    with open(filename, encoding='utf-8') as a_file:
        line_count = len(list(a_file))
        if nb_lines >= line_count or nb_lines <= 0:
            nb_lines = line_count
        a_file.seek(0)
        for line in range(nb_lines):
            print(a_file.readline(), end='')
