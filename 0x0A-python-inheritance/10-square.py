#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle
"Module"


class Square(Rectangle):
    """
    Square class
    """
    def __init__(self, size):
        self.integer_validator(size)
        self.__size = size

    def area(self):
        return area ** 2
