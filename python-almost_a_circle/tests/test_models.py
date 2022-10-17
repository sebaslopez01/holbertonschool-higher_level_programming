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
        ins = Base(89)
        self.assertEqual(ins.id, 89)
