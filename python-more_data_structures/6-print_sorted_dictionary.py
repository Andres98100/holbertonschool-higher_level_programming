#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    if a_dictionary == {}:
        return
    new_key = a_dictionary.keys()
    new_sorted = sorted(new_key)
    new_dictionary = {}
    for i in new_sorted:
        new_dictionary[i] = a_dictionary[i]
    print('\n'.join("{}: {}".format(k, v)for k, v in new_dictionary.items()))
    return new_dictionary
