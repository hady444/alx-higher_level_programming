#!/usr/bin/python3
"""Module"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    BaseGeometry class
    """
    def __init__(self, width, height):
        self.integer_validator("width", widht)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
