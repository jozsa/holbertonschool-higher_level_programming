#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if type(tuple_a) and type(tuple_b) is tuple:
        len_a = len(tuple_a)
        len_b = len(tuple_b)
        tuple_a = tuple(x if x else '0' for x in tuple_a)
        tuple_b = tuple(x if x else '0' for x in tuple_b)
        if len_a or len_b < 2:
            for i in range(2):
                tuple_a = tuple_a + (0,)
                tuple_b = tuple_b + (0,)
        total_a = tuple_a[0] + tuple_b[0]
        total_b = tuple_a[1] + tuple_b[1]
        total_tuple = (total_a, total_b)
    return total_tuple
