#!/usr/bin/python3
def safe_print_integer(value):
    safe = int(value)
    try:
        print("{:d}".format(int(value)))
        return True
    except (ValueError, TypeError):
        return False
