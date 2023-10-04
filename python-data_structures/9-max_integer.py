#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list is None:
        return None
    else:
        new_list = my_list.copy()  # copy the list
        new_list.sort(reverse=True)  # sort the list
        return new_list[0]
