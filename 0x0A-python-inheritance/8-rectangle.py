#!/usr/bin/python3
"""Module"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    BaseGeometry class
    """
    def __init__(self, width, height):
        BaseGeometry.integer_validator("width", widht)
        self.__width = width
        BaseGeometry.integer_validator("height", height)
        self.__height = height
