#!/usr/bin/python3
def best_score(a_dictionary):
    result = dict(map(lambda x: (x[0], x[1] < x[1]), a_dictionary.items()))
    return result
