#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) != str or not roman_string:
        return 0
    set_roman = {"I": 1, "V": 5, "X": 10, "L": 50,
                 "C": 100, "D": 500, "M": 1000}
    total = 0
    for i in range(len(roman_string) - 1, - 1, -1):
        set_integer = set_roman[roman_string[i]]
        if 4 * set_integer < total:
            total -= set_integer
        else:
            total += set_integer
    return total
