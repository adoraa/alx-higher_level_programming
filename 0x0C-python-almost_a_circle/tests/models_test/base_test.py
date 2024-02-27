#!/usr/bin/python3
"""Defines unittests for base.py"""
import unittest
import os
from models.base import Base


class TestBase(unittest.TestCase):

    def setUp(self):
        self.clean_up()

    def tearDown(self):
        self.clean_up()

    def clean_up(self):
        test_files = ['Base.json']
        for file in test_files:
            if os.path.exists(file):
                os.remove(file)

    def test_init_with_id(self):
        obj = Base(5)
        self.assertEqual(obj.id, 5)

    def test_init_without_id(self):
        obj = Base()
        self.assertEqual(obj.id, 1)

    def test_to_json_string_empty_list(self):
        result = Base.to_json_string([])
        self.assertEqual(result, "[]")

    def test_to_json_string_non_empty_list(self):
        result = Base.to_json_string([{'id': 1, 'name': 'test'}])
        self.assertEqual(result, '[{"id": 1, "name": "test"}]')

    def test_to_json_string_none_list(self):
        result = Base.to_json_string(None)
        self.assertEqual(result, "[]")

    def test_save_to_file(self):
        obj = Base(1)
        Base.save_to_file([obj])
        with open('Base.json', 'r') as file:
            content = file.read()
        self.assertEqual(content, '[{"id": 1}]')

    def test_from_json_string_empty_string(self):
        result = Base.from_json_string("")
        self.assertEqual(result, [])

    def test_from_json_string_non_empty_string(self):
        result = Base.from_json_string('[{"id": 1, "name": "test"}]')
        self.assertEqual(result, [{'id': 1, 'name': 'test'}])

    def test_create(self):
        instance = Base.create(id=1, name='test')
        self.assertEqual(instance.id, 1)
        self.assertEqual(instance.name, 'test')

    def test_load_from_file_file_not_exist(self):
        result = Base.load_from_file()
        self.assertEqual(result, [])

    def test_load_from_file_file_exist(self):
        obj = Base(1)
        Base.save_to_file([obj])
        result = Base.load_from_file()
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].id, 1)

if __name__ == '__main__':
    unittest.main()
