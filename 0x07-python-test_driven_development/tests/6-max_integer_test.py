#!/usr/bin/python3
import unittest
# 6-max_integer_test.py
"""
Unittests for max_integer([..]).
"""

max_integer = __import__('6-max_integer').max_integer

class MaxIntegerTest(unittest.TestCase):
    def test_empty_list(self):
        result = max_integer([])
        self.assertIsNone(result)

    def test_positive_numbers(self):
        result = max_integer([1, 2, 3, 4, 5])
        self.assertEqual(result, 5)

    def test_negative_numbers(self):
        result = max_integer([-1, -2, -3, -4, -5])
        self.assertEqual(result, -1)

    def test_mixed_numbers(self):
        result = max_integer([-5, 0, 10, -2, 8])
        self.assertEqual(result, 10)

    def test_duplicate_numbers(self):
        result = max_integer([1, 2, 2, 3, 3, 3])
        self.assertEqual(result, 3)

    def test_single_number(self):
        result = max_integer([10])
        self.assertEqual(result, 10)

    def test_float_numbers(self):
        result = max_integer([1.5, 2.3, 0.8, 4.2])
        self.assertEqual(result, 4.2)

    def test_empty_list_with_default_argument(self):
        result = max_integer()
        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()
