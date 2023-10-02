#!/usr/bin/python3
def replace_in_list(my_list, idx, element):  # define method
    if idx < 0 or idx > len(my_list) - 1:  # move along the list
        return my_list
    else:
        my_list.insert(idx, element)  # insert element at idx
