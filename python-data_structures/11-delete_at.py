#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if my_list is None:
        return None
    if idx < 0 or idx > len(my_list):  # if idx is negative or out of range
        return my_list
    else:
        del my_list[idx]  # delete the element at idx
    return my_list
