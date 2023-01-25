#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
if __name__ == "__main__":
    a = 10
    b = 5
    result_add = add(a, b)
    result_substract = sub(a, b)
    result_multiply = mul(a, b)
    result_divide = div(a, b)
    print("{} + {} = {}".format(a, b, result_add))
    print("{} - {} = {}".format(a, b, result_substract))
    print("{} * {} = {}".format(a, b, result_multiply))
    print("{} / {} = {}".format(a, b, result_divide))
