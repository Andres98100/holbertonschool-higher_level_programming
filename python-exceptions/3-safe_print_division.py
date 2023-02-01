#!/usr/bin/python3
def safe_print_division(a, b):
    result = None
    try:
        result = a / b
    except ZeroDivisionError:
        return result
    finally:
        print("Inside result: {}".format(result))
    return result
