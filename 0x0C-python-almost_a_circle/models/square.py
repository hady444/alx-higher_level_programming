#!/usr/bin/python3
"""Square Module"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Class Square inherites from Rectangle class"""

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return f"[{type(self).__name__}] ({self.id}) \
                {self.x}/{self.y} - {self.height}"

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value <= 0:
            raise ValueError("size must be > 0")
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        if args == ():
            for kw, val in kwargs.items():
                setattr(self, kw, val)

        attribute_names = ['id', 'size', 'x', 'y']

        for name, value in zip(attribute_names, args):
            setattr(self, name, value)

    def to_dictionary(self):
        return {
                'id': self.id,
                'size': self.size,
                'x': self.x,
                'y': self.y
        }
