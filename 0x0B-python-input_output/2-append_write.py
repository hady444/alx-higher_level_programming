#!/usr/bin/python3
"""Module"""


def append_write(filename="", text=""):
    """read text file with UTF-8
    Args:
        filename (str): file passed with extension. Defaults to "".
    """
    with open(file=filename, mode="a",encoding="UTF8") as f:
        return f.write()
