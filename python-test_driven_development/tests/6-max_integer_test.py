#!/usr/bin/python3
import unittest

"""
This module defines max_integer function
"""


def max_integer(list=[]):
    """Function to find and return the max integer in a list of integers
        If the list is empty, the function returns None
    """
    if len(list) == 0:
        return None
    result = list[0]
    i = 1
    while i < len(list):
        if list[i] > result:
            result = list[i]
        i += 1
    return result


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
