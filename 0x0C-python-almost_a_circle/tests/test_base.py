#!/usr/bin/python3
"""Module"""
import unittest
from models.base import Base
class Test_base(unittest.TestCase):
    """Test class"""

    def setUp(self):
        '''Imports module, instantiates class'''
        Base._Base__nb_objects = 0
        pass

    def tearDown(self):
        '''Cleans up after each test_method.'''
        pass

    def test_id_passed(self):
        base = Base(6)
        self.assertEqual(base.id, 6)

    def test_none_id(self):
        a = Base()
        b = Base()
        self.assertEqual(b.id, 2)
