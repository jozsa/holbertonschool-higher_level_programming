#!/usr/bin/python3
def uniq_add(my_list=[]):
    result = 0
    for element in my_list:
        occurences = my_list.count(element)
        result += element / occurences
    return int(result)
