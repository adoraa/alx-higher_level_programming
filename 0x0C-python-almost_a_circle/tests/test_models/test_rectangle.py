#!/usr/bin/python3
"""Defines unittests for rectangle.py."""
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):

    def test_init(self):
        r = Rectangle(5, 10, 2, 3, 1)
        self.assertEqual(r.id, 1)
        self.assertEqual(r.width, 5)
        self.assertEqual(r.height, 10)
        self.assertEqual(r.x, 2)
        self.assertEqual(r.y, 3)

    def test_area(self):
        r = Rectangle(5, 10)
        self.assertEqual(r.area(), 50)

    def test_display(self):
        r = Rectangle(3, 2)
        expected_output = "###\n###"
        with unittest.mock.patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            r.display()
        self.assertEqual(mock_stdout.getvalue().strip(), expected_output)

    def test_str(self):
        r = Rectangle(4, 5, 1, 2, 10)
        expected_output = "[Rectangle] (10) 1/2 - 4/5"
        self.assertEqual(str(r), expected_output)

    def test_update(self):
        r = Rectangle(2, 3, 1, 1)
        r.update(5, 6, 7, 8, 9)
        self.assertEqual(r.id, 5)
        self.assertEqual(r.width, 6)
        self.assertEqual(r.height, 7)
        self.assertEqual(r.x, 8)
        self.assertEqual(r.y, 9)

    def test_to_dictionary(self):
        r = Rectangle(4, 5, 1, 2, 10)
        expected_output = {'id': 10, 'width': 4, 'height': 5, 'x': 1, 'y': 2}
        self.assertEqual(r.to_dictionary(), expected_output)

if __name__ == '__main__':
    unittest.main()
