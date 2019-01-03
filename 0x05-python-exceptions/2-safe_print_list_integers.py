#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    length = 0
    for element in my_list[:x]:
        try:
            print('{:d}'.format(element), end='')
            length += 1
        except (TypeError, ValueError):
            pass
    print('')
    return length