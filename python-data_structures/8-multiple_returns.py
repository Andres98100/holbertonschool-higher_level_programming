#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) == "":
        sentence[0] = None
    len_str = len(sentence)
    char = sentence[0]
    return len_str, char