#!/usr/bin/python3
"""Module"""


def append_after(filename="", search_string="", new_string=""):
    """append new string after each line search string is in.

    Args:
        filename (str): path to file. Defaults to "".
        search_string (str): string to search for. Defaults to "".
        new_string (str): string to write. Defaults to "".
    """
    with open(filename, 'r+', encoding='UTF-8') as f:
        lines = f.readlines()
        f.seek(0)
        for line in lines:
            f.write(line)
            if line.find(search_string) != -1:
                f.write(new_string)
