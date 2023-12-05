#!/usr/bin/python3
"""
Module
"""


def write_file(filename="", text=""):
    """write text to file with UTF-8
    Args:
        filename (str): file passed with extension. Defaults to "".
        text (str): text. Defaults to ""
    Return:
        number of chars written
    """
    with open(filename, mode="w", encoding="UTF8") as f:
        return f.write(text)
