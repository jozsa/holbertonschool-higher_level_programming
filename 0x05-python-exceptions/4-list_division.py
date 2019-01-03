#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = 0
    div_list = []
    for index in range(list_length):
            try:
                result = my_list_1[index] / my_list_2[index]
            except TypeError:
                result = 0
                print('wrong type')
            except ZeroDivisionError:
                result = 0
                print('division by 0')
            except IndexError:
                result = 0
                print('out of range')
            finally:
                div_list.append(result)
    return div_list
