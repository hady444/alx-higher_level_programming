#!/usr/bin/python3
"""
Module
"""


import unittest


def max_integer(list=[]):
    """Get max number

    Args:
        list (list):list contain numbers. Defaults to [].
    Return:
        max number
    """
    return max(list)


class TestMaxInteger(unittest.TestCase):
    """
    class Test my function
    """
    def Test_Max_End(self):
        self.assertEqual(max_integer([10, 100, 300, 5000]), 5000)

    def Test_Max_Begin(self):
        self.assertEqual(max_integer([5000, 10, 100, 300]), 5000)

    def Test_Max_Middle(self):
        self.assertEqual(max_integer([10, 20, 15000, 300, 5000]), 15000)

    def Test_one_Negative(self):
        self.assertEqual(max_integer([10, 100, 300, -5000]), 300)

    def Test_All_Negative(self):
        self.assertEqual(max_integer([-10, -100, -300, -5000]), -10)

    def Test_One_Element(self):
        self.assertEqual(max_integer([10]), 10)

    def Test_Is_empty(self):
        with self.assertRaises(ValueError):
            max_integer([])
