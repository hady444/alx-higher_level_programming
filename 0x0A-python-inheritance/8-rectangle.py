#!/usr/bin/python3
"""Module"""


class Rectangle(BaseGeometry):
    """
    BaseGeometry class
    """
    def __init__(self, width, height):
        BaseGeometry.integer_validator("width", widht)
        self.width = width
        BaseGeometry.integer_validator("width", height)
        self.height = height
