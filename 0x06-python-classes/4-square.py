#!/usr/bin/python3
"""Square module"""


class Square:
    """Square4"""
    def __init__(self, size=0):
        self.__size = size
        if not (isinstance(size, int)):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    @property
    def size(self):
        """getter"""
        return self.__size

    @size.setter
    def size(self, size=0):
        """setter"""
        self.__size = size
        if not (isinstance(size, int)):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        return self.__size**2
