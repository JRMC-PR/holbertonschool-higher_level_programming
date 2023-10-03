#!/urs/bin/python3
def multiple_returns(sentence):
    if sentence is None:  # if sentence == None:
        return (0, None)
    else:
        # return (len(sentence), sentence[:1])
        return (len(sentence), sentence[0])
