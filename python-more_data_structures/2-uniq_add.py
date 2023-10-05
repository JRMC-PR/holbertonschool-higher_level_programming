#!/usr/bin/python3
def uniq_add(my_list=[]):
    if my_list == None:
        return None
    for i in range(len(my_lyst)):
        if my_list[i] != my_list[i - 1]:
            res += my_list[i]
    return my_list
