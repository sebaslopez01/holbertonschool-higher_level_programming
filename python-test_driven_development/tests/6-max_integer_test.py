#!/usr/bin/python3
import unittest

"""
This module defines max_integer function
"""

max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_max_integer(self):
        self.assertEqual(max_integer([1, 2, 4, 3]), 4)

    def test_max_at_the_end(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_max_at_the_beginning(self):
        self.assertEqual(max_integer([4, 2, 3, 1]), 4)

    def test_max_at_the_middle(self):
        self.assertEqual(max_integer([1, 2, 5, 4, 3]), 5)

    def test_one_negative_number(self):
        self.assertEqual(max_integer([1, 2, -3, 4]), 4)

    def test_only_negative_numbers(self):
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_only_one_element(self):
        self.assertEqual(max_integer([1]), 1)

    def test_list_empty(self):
        self.assertEqual(max_integer([]), None)
