#!/usr/bin/python3
"""Module"""


class BaseGeometry:
    """
    BaseGeometry class
    """
    def __init__(self, width, height):
        integer_validator("width", widht)
        self.width = width
        integer_validator("width", height)
        self.height = height

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
