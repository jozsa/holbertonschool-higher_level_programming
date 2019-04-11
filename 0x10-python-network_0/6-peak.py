#!/usr/bin/python3
"""
Only one function: find_peak(list_of_integers)
Find the peak of a list of unsorted integers
"""


def find_peak(list_of_integers):
    """
    Returns the first peak found in a list
    of unsorted integers
    """
    if not list_of_integers:
        return None
    length = len(list_of_integers)
    if length == 1 or length == 2:
        if length == 2:
            if list_of_integers[0] > list_of_integers[1]:
                return list_of_integers[0]
            else:
                return list_of_integers[1]
    if list_of_integers[0] > list_of_integers[1]:
        return list_of_integers[0]
    if list_of_integers[-1] > list_of_integers[-2]:
        return list_of_integers[-1]
    if length % 2:
        middle = int(length / 2)
    else:
        middle = int((length / 2) - 1)
    if list_of_integers[middle] > list_of_integers[middle + 1] \
            and list_of_integers[middle] > list_of_integers[middle - 1]:
        return list_of_integers[middle]
    if list_of_integers[middle + 1] > list_of_integers[middle]:
        return find_peak(list_of_integers[middle:])
    else:
        return find_peak(list_of_integers[:middle])
