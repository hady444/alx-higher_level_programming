#!/usr/bin/python3
"""
Module
"""


def read_file(filename=""):
    """read text file with UTF-8
    Args:
        filename (str): file passed with extension. Defaults to "".
    """
    with open(file=filename, encoding="UTF8") as f:
        print(f.read())
