#!/usr/bin/python3
"""Module"""
from models.base import Base


class Rectangle(Base):
    """Rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    def __str__(self):
        """str"""
        return f"[{type(self).__name__}] ({self.id}) " +\
            f"{self.x}/{self.y} - {self.width}/{self.height}"

    @property
    def width(self):
        '''width'''
        return self.__width

    @width.setter
    def width(self, value):
        '''width'''
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        '''height'''
        return self.__height

    @height.setter
    def height(self, value):
        '''height'''
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        '''  '''
        return self.__x

    @x.setter
    def x(self, value):
        '''  '''
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return (self.__y)

    @y.setter
    def y(self, value):
        '''  '''
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        '''Computes area of this rectangle.'''
        return self.width * self.height

    def display(self):
        for _ in range(self.y):
            print()
        for _ in range(self.__height):
            for _ in range(self.x):
                print(end=" ")
            for _ in range(self.__width):
                print("#", end='')
            print("")
