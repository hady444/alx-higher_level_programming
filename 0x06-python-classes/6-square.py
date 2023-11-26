#!/usr/bin/bash
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
    def size(self, size):
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
    def position(self, value):
        """Setter method"""
        if (not isinstance(num, tuple) or
                len(value) != 2 or
                not all(isinstance(n, int) for n in value) or
                not all(n >= 0 for n in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

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
