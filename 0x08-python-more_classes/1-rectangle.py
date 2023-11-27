#!/usr/bin/python3
"""Module"""


class Rectangle:
    """
    Rectangle 1
    """

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
    
    @property
    def width(self):
        return self.__width
    
    @width.setter
    def width(self, width):
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width
    
    @property
    def height(self):
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        return self.__height
    
    @height.setter
    def height(self, height):
        self.__height = height
