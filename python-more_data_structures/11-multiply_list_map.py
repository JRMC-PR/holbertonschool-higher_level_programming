#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    # map(function_to_apply, list_of_inputs)
    return list(map(lambda x: x * number, my_list))
