#!/usr/bin/python3
class LockedClass:
    def __setattr__(self, name, val):
        if name != "first_name":
            raise AttributeError(f'LockedClass object has no attribute {name}')
