#!/usr/bin/python3
"""Unittest for max_integer([..])
"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """*** writing unittests for the function***"""

    def test_orderedList(self):
        """Testing the muximum element in an ordered list."""
        ordered = [11, 22, 33, 44]
        self.assertEqual(max_integer(ordered), 44)

    def test_unorderedList(self):
        """Testing the muximum element in an ordered list."""
        unordered = [11, 22, 44, 33]
        self.assertEqual(max_integer(unordered), 44)

    def test_maxAtBegginning(self):
        """Testing a list whose first element is the maximum"""
        max_at_beginning = [44, 33, 22, 11]
        self.assertEqual(max_integer(max_at_beginning), 44)

    def test_emptyList(self):
        """Testing an empty list"""
        empty = []
        self.assertEqual(max_integer(empty), None)

    def test_oneElementList(self):
        """Testing a single element list"""
        one_element = [10]
        self.assertEqual(max_integer(one_element), 10)

    def test_floatNumbes(self):
        """Testing a list containing float numbers"""
        floats = [1.1, 2.2, -3.3, 4.4]
        self.assertEqual(max_integer(floats), 4.4)

    def test_intsAndFloats(self):
        """Testing a list conatining both integer and float numbers"""
        ints_and_floats = [1, 2.2, -3, 4.4, 2]
        self.assertEqual(max_integer(ints_and_floats), 4.4)

    def test_string(self):
        """Testing a string."""
        string = "walter"
        self.assertEqual(max_integer(string), 'w')

    def test_listOfStrings(self):
        """Testing a list of strings."""
        strings = ["walter", "white", "jr"]
        self.assertEqual(max_integer(strings), "white")

    def test_emptyString(self):
        """Testing an empty string."""
        self.assertEqual(max_integer(""), None)


if __name__ == '__main__':
    unittest.main()
