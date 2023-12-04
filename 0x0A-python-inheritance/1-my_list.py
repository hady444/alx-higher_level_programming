#!/usr/bin/python3
"""
inherits from list class
"""

class MyList(list):
    """inherits from list

    Args:
        list (_class_): class list inherited
    """

    def print_sorted(self):
        print(sorted(self))
