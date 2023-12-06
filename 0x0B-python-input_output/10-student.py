#!/usr/bin/python3
"""Module"""


class Student:
    """
    Student class
    """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if (attrs is None):
            return self.__dict__
        my_dictionary = {}
        for k, val in self.__dict__.items():
            if k in attrs:
                my_dictionary[k] = val
        return (my_dictionary)
