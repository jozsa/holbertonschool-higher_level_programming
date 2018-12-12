#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    size = len(my_list)
    if size > idx >= 0:
        del my_list[idx]
    return my_list
