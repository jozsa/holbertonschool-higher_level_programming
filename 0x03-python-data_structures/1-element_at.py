#!/usr/bin/python3
def element_at(my_list, idx):
    size = len(my_list)
    if idx > size - 1 or idx < 0:
        return None
    else:
        return my_list[idx]
