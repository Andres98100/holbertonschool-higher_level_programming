#!/usr/bin/python3
def best_score(a_dictionary):
    result = dict(map(lambda x: (x[0], max(x[1])), a_dictionary.items()))
    return result
