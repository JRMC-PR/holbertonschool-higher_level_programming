#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if my_list is None:
        return None
    elif search == replace:
        return my_list
    new_list = my_list.copy()
    for i in range(len(new_list) - 1):
        if new_list[i] == search:
            new_list[i] = replace
    return new_list
