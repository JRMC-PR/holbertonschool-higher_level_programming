#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:  # if list is empty
        return None
    # new_list = my_list.copy()  # copy the list
    my_list.sort(reverse=True)  # sort the list
    return my_list[0]
