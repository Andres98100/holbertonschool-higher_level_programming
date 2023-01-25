#!/usr/bin/python3
from calculator_1.py import add, subtract, multiply, divide
if __name__ == "__main__":
    a = 10
    b = 5
    result_add = add(a, b)
    result_substract = subtract(a, b)
    result_multiply = multiply(a, b)
    result_divide = divide(a, b)
    print("{} + {} = {}".format(a, b, result_add))
    print("{} - {} = {}".format(a, b, result_substract))
    print("{} * {} = {}".format(a, b, result_multiply))
    print("{} / {} = {}".format(a, b, result_divide))
