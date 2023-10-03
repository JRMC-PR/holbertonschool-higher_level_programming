#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list is None:
        return None
    else:
        new_list = my_list.copy()
        new_list.sort()
        return new_list[-1]
