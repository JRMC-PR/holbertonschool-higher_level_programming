#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence is None or sentence == "":  # if sentence == None:
        return (0, None)
    else:
        # return (len(sentence), sentence[][])
        return (len(sentence), sentence[0][0])
