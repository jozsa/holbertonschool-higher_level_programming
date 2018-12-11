#!/usr/bin/python3
def no_c(my_string):
    new_string = list(my_string)
    new_string = [c for c in new_string if c not in 'cC']
    new_string = ''.join(new_string)
    return new_string
