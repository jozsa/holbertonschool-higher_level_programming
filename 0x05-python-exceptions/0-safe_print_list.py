#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    length = 0
    try:
        for element in my_list[:x]:
            length += 1
        print(''.join(str(i) for i in my_list[:x]))
    except Exception:
        print('Could not print list')
    return length
