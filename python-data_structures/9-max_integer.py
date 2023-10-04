#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list is None:
        return None
    # new_list = my_list.copy()  # copy the list
    my_list.sort(reverse=True)  # sort the list
    return my_list[0]
