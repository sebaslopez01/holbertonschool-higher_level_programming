#!/usr/bin/python3

"""

This module defines test classes

"""

import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestModels(unittest.TestCase):
    def test_save_id(self):
        self.assertEqual(Base(89).id, 89)

    def test_to_json_string(self):
        self.assertEqual(Base.to_json_string(None), '[]')
