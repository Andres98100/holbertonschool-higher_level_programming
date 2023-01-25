#!/usr/bin/python3
from calculator_1.py import add, substract, multiply, divide
if __name__ == "__main__":
    a = 10
    b = 5
    result_add = add(a, b)
    result_substract = substract(a, b)
    result_multiply = multiply(a, b)
    result_divide = divide(a, b)
    print("{}".format(result_add))
    print("{}".format(result_substract))
    print("{}".format(result_multiply))
    print("{}".format(result_divide))
