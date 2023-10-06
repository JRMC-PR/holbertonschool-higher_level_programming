#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None or a_dictionary == {}:
        # if a_dictionary is None or if a_dictionary is empty
        return None
    else:
        # return the key with the highest value
        return max(a_dictionary, key=a_dictionary.get)
