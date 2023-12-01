#!/usr/bin/python3
"""
Module
"""


def text_indentation(text):
    """function that prints a text with 2 new lines after each of
        these characters: ., ? and :

    Args:
        text (str): text provided
    Raises:
        Type Error: text must be a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for letter in text:
        print(letter, end='')
        if (letter in [':', '?', '.']):
            print("\n")
