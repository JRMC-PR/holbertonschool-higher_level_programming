#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
from max_integer import max_integer


class TestMaxInteger(unittest.TestCase):
    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_one_element_list(self):
        self.assertEqual(max_integer([1]), 1)

    def test_positive_numbers(self):
        self.assertEqual(max_integer([1, 2, 3]), 3)
        self.assertEqual(max_integer([3, 2, 1]), 3)
        self.assertEqual(max_integer([2, 3, 1]), 3)

    def test_negative_numbers(self):
        self.assertEqual(max_integer([-1, -2, -3]), -1)
        self.assertEqual(max_integer([-3, -2, -1]), -1)
        self.assertEqual(max_integer([-2, -3, -1]), -1)

    def test_mixed_numbers(self):
        self.assertEqual(max_integer([-1, 2, 3]), 3)
        self.assertEqual(max_integer([3, -2, 1]), 3)
        self.assertEqual(max_integer([2, 3, -1]), 3)

    def test_float_numbers(self):
        self.assertEqual(max_integer([1.0, 2.0, 3.0]), 3.0)
        self.assertEqual(max_integer([3.0, 2.0, 1.0]), 3.0)
        self.assertEqual(max_integer([2.0, 3.0, 1.0]), 3.0)

    def test_sorted(self):
        """Test a sorted list of integers"""
        ordered = [32, 64, 128, 256]
        self.assertEqual(max_integer(ordered), 256)

    def test_sorted_rev(self):
        """Test a sorted (in reverse) list of integers"""
        ordered = [1024, 512, 256, 128, 64]
        self.assertEqual(max_integer(ordered), 1024)


if __name__ == '__main__':
    unittest.main()
