#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Tests for the max_integer function."""

    def test_ordered_list(self):
        """Max is found when the list is already sorted ascending."""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        """Max is found when the list is in a random order."""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_descending_list(self):
        """Max is found when the list is sorted descending."""
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_single_element(self):
        """A single-element list returns that element."""
        self.assertEqual(max_integer([5]), 5)

    def test_empty_list(self):
        """An empty list returns None."""
        self.assertEqual(max_integer([]), None)

    def test_default_argument(self):
        """Calling with no argument at all returns None."""
        self.assertEqual(max_integer(), None)

    def test_negative_numbers(self):
        """Max is found correctly among negative numbers."""
        self.assertEqual(max_integer([-5, -1, -10]), -1)

    def test_mixed_sign_numbers(self):
        """Max is found correctly among positive and negative numbers."""
        self.assertEqual(max_integer([-5, 3, -1, 10, 2]), 10)

    def test_duplicate_max(self):
        """Max is found correctly when the max value repeats."""
        self.assertEqual(max_integer([4, 4, 2, 1]), 4)

    def test_all_same_value(self):
        """Max is found correctly when every element is identical."""
        self.assertEqual(max_integer([7, 7, 7]), 7)


if __name__ == "__main__":
    unittest.main()
