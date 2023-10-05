#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if my_list is None:
        return None
    list_c = my_list.copy()
    for i in range(len(list_c) - 1):
        if i == search:
            list_c[i] = replace
            return list_c
