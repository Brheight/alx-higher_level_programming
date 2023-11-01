#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_max_integer(self):
        # Test with a list of integers
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

        # Test with a list of integers in a different order
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

        # Test with an empty list
        self.assertEqual(max_integer([]), None)

        # Test with a single-element list
        self.assertEqual(max_integer([5]), 5)

        # Test with a list containing negative numbers
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

        # Test with a list containing positive and negative numbers
        self.assertEqual(max_integer([1, -2, 3, -4]), 3)

if __name__ == '__main__':
    unittest.main()
