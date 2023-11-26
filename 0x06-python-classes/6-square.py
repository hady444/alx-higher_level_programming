#!/usr/bin/python3
"""Square module"""


class Square:
    """Square6"""
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """getter"""
        return self.__position

    @position.setter
    def size(self, position=(0, 0)):
        """setter"""
        self.__position = position
        if type(self.__position) != tuple or len(self.__position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        return self.__size**2

    def my_print(self):
        if self.__size == 0:
            print()
            return
        for _ in range(self.__position[1]):
            print()
        for _ in range(self.__size):
            for _ in range(self.__position[0]):
                print(" ", end='')
            for _ in range(self.__size):
                print("#", end='')
            print()