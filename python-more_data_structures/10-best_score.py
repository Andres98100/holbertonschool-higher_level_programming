#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    aux = 0
    aux_key = ""
    for key, value in a_dictionary.items():
        if value > aux:
            aux = value
            aux_key = key
    return aux_key
