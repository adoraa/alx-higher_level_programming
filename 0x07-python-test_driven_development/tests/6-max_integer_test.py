#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """unittest class for max_integer"""
    def test_module_docstring(self):
        """Tests for module docsting"""
        m = __import__('6-max_integer').__doc__
        self.assertTrue(len(m) > 1)

    def test_function_docstring(self):
        """Tests for funstion docstring"""
        f = max_integer.__doc__
        self.assertTrue(len(f) > 1)

    def test_positive_numbers(self):
        """Tests for all positive with max at end"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_mixed_numbers(self):
        """Tests for all positive with max in middle"""
        self.assertEqual(max_integer([1, 3, 5, 4, 2]), 5)

    def test_empty_list(self):
        """Tests for empty list []"""
        self.assertIsNone(max_integer([]))

    def test_negative_numbers(self):
        """Tests for list with all negative numbers"""
        self.assertEqual(max_integer([-1, -5, -3, -7]), -1)

    def test_duplicate_numbers(self):
        """Tests for list with duplicate numbers"""
        self.assertEqual(max_integer([1, 2, 2, 1]), 2)

    def test_single_number(self):
        """Tests for only one number in the list"""
        self.assertEqual(max_integer([5]), 5)

    def test_float_numbers(self):
        """Tests for list with floats"""
        self.assertEqual(max_integer([1.5, 2.5, 3.5]), 3.5)

    def test_mixed_float_and_integer(self):
        """Tests for list with int and float"""
        self.assertEqual(max_integer([1, 2.5, 3]), 3)


if __name__ == '__main__':
    unittest.main()
