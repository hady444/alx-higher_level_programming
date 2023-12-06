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
        i = -1
        for line in f.readlines():
            i += len(line)
            if line.find(search_string) != -1:
                f.seek(i)
                f.write(new_string)
