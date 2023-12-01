#!/usr/bin/python3
"""
Module
"""


import unittest
max_integer = __import__('6-max_integer').max_integer


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
        with self.assertRaises(TypeError):
            max_integer([])

if __name__ == '__main__':
    unittest.main()
