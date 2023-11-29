#!/usr/bin/python3
"""
Module
"""

class LockedClass:
    """
    LockedClass with no class or object attribute, that prevents the user from
    dynamically creating new instance attributes, except if the new instance
    attribute is called first_name.
    
    Methods:
        __setattr__(self, name, value): Restrict the creation of instance attribute
    
    Example:
        lc = LockedClass()
        lc.first_name = "John"
        try:
            lc.last_name = "Snow"
        except Exception as e:
            print("[{}] {}".format(e.__class__.__name__, e))
    Output:
        [AttributeError] 'LockedClass' object has no attribute 'last_name'
    """

    def __setattr__(self, name, val):
        """
        Restrict the creation of instance attribute

        Args:
            name (str): name of attribute
            val: the value to be assigned
        Raises:
            AttributeError: if the name of attribute not equal 'first_name'
        """

        if name != "first_name":
            raise AttributeError(f'LockedClass object has no attribute {name}')
