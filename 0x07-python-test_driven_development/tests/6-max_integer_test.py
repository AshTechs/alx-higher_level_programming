#!/usr/bin/python3

import unittest
from my_module import max_integer

class TestMaxInteger(unittest.TestCase):
    def test_regular_values(self):
        self.assertEqual(max_integer([1, 3, 5, 2]), 5)
        self.assertEqual(max_integer([-1, -3, -5, -2]), -1)

    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_float_values(self):
        self.assertAlmostEqual(max_integer([1.5, 3.7, 2.8]), 3.7)
        self.assertAlmostEqual(max_integer([-1.5, -3.7, -2.8]), -1.5)

    def test_mixed_values(self):
        self.assertEqual(max_integer([1, 3.7, 5, 2]), 5)
        self.assertEqual(max_integer([-1, -3.7, -5, -2]), -1)

    def test_duplicate_values(self):
        self.assertEqual(max_integer([5, 5, 5]), 5)
        self.assertEqual(max_integer([-5, -5, -5]), -5)

    def test_single_value(self):
        self.assertEqual(max_integer([5]), 5)
        self.assertEqual(max_integer([-5]), -5)

if __name__ == '__main__':
    unittest.main()

