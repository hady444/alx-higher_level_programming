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
    for delim in ".?:":
        #print(delim, text.split(delim))
        text = (delim + "\n\n").join(
            [line.strip(" ") for line in text.split(delim)])

    print(text, end="")
