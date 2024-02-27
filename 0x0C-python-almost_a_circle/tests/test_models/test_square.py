#!/usr/bin/python3
"""Defines unittests for models/square.py"""
import unittest
from models.square import Square


class TestSquare(unittest.TestCase):

    def test_init(self):
        s = Square(5, 2, 3, 1)
        self.assertEqual(s.id, 1)
        self.assertEqual(s.size, 5)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.y, 3)

    def test_area(self):
        s = Square(5)
        self.assertEqual(s.area(), 25)

    def test_display(self):
        s = Square(3)
        expected_output = "###\n###\n###"
        with unittest.mock.patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            s.display()
        self.assertEqual(mock_stdout.getvalue().strip(), expected_output)

    def test_str(self):
        s = Square(4, 1, 2, 10)
        expected_output = "[Square] (10) 1/2 - 4"
        self.assertEqual(str(s), expected_output)

    def test_update(self):
        s = Square(2, 1, 1)
        s.update(5, 6, 7, 8)
        self.assertEqual(s.id, 5)
        self.assertEqual(s.size, 6)
        self.assertEqual(s.x, 7)
        self.assertEqual(s.y, 8)

    def test_to_dictionary(self):
        s = Square(4, 1, 2, 10)
        expected_output = {'id': 10, 'size': 4, 'x': 1, 'y': 2}
        self.assertEqual(s.to_dictionary(), expected_output)

if __name__ == '__main__':
    unittest.main()
