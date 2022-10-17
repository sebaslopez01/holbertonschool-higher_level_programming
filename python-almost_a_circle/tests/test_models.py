#!/usr/bin/python3

"""

This module defines test classes

"""

import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestModels(unittest.TestCase):
    def test_assigning_automatically_id(self):
        self.assertEqual(Base().id, 1)

    def test_assigning_automatically_id_plus_one(self):
        self.assertEqual(Base().id, 2)

    def test_save_id(self):
        self.assertEqual(Base(89).id, 89)

    def test_to_json_string_none(self):
        self.assertEqual(Base.to_json_string(None), '[]')

    def test_to_json_string_empty(self):
        self.assertEqual(Base.to_json_string([]), '[]')

    def test_to_json_string_exists(self):
        self.assertEqual(Base.to_json_string([{'id': 12}]), '[{"id": 12}]')

    def test_from_json_string_none(self):
        self.assertEqual(Base.from_json_string(None), [])

    def test_from_json_string_empty(self):
        self.assertEqual(Base.from_json_string("[]"), [])

    def test_from_json_string_exists(self):
        self.assertEqual(Base.from_json_string('[{ "id": 89 }]'), [{'id': 89}])
