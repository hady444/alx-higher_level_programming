#!/usr/bin/python3
"""Module"""


class Student:
    """
    Student class
    """

    def __init__(self, first_name, last_name, age):
        self.firstname = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        return (vars(self))
