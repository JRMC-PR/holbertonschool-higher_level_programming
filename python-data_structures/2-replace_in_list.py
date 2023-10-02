#!/usr/bin/python3
def replace_in_list(my_list, idx, element):  # define method
    if idx < 0 or idx > len(my_list) - 1:  # check if idx is out of range
        return my_list  # return the list
    else:
        my_list[idx] = element
        return my_list
