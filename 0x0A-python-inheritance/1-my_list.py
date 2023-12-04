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
        # sorted method
        # sorted(iterable[, key][, reverse])
        print(sorted(self))
