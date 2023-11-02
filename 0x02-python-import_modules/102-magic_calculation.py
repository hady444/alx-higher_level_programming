#!/usr/bin/python3
def magic_calculation(a, b):
    if a < b:
        add = __import__("magic_calculation_102").add
        return add(a, b)
    return __import__("magic_calculation_102").sub(a, b)
