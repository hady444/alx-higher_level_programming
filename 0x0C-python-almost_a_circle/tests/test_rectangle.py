#!/usr/bin/python3
"""Module"""

import unittest
from models.rectangle import Rectangle
from models.base import Base
class Test_Rec(unittest.TestCase):
    """Class test Rectangle"""

    def setUp(self):
        Base.__nb_objects = 0

    def tearDown(self):
        pass

    def test_no_id(self):
        print(Base.__nb_objects)
        rec = Rectangle(4, 5, 1, 2)
        self.assertEqual(rec.id, 1)
