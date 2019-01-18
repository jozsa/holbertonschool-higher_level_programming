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
    line_count = 0
    with open(filename, encoding='utf-8') as a_file:
        for line in a_file:
            if line_count < nb_lines:
                print(line, end='')
            line_count += 1
        if nb_lines >= line_count or nb_lines <= 0:
            a_file.seek(0)
            print(a_file.read(), end='')
