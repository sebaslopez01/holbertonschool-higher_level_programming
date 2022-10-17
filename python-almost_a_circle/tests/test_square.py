#!/usr/bin/python3

"""

This module defines TestSquare class

"""

from io import StringIO
import unittest
from unittest.mock import patch
from models.square import Square


class TestSquare(unittest.TestCase):
    def test_Square_creation_1(self):
        square = Square(1)
        self.assertEqual(square.size, 1)

    def test_Square_creation_2(self):
        square = Square(1, 2)
        self.assertEqual(square.size, 1)
        self.assertEqual(square.x, 2)

    def test_Square_creation_3(self):
        square = Square(1, 2, 3)
        self.assertEqual(square.size, 1)
        self.assertEqual(square.x, 2)
        self.assertEqual(square.y, 3)

    def test_Square_size_raise_type_error(self):
        with self.assertRaises(TypeError):
            Square("1")

    def test_Square_x_raise_type_error(self):
        with self.assertRaises(TypeError):
            Square(1, "2")

    def test_Square_y_raise_type_error(self):
        with self.assertRaises(TypeError):
            Square(1, 2, "3")

    def test_Square_creation_4(self):
        square = Square(1, 2, 3, 4)
        self.assertEqual(square.size, 1)
        self.assertEqual(square.x, 2)
        self.assertEqual(square.y, 3)
        self.assertEqual(square.id, 4)

    def test_Square_size_raise_value_error(self):
        with self.assertRaises(ValueError):
            Square(-1)

    def test_Square_x_raise_value_error(self):
        with self.assertRaises(ValueError):
            Square(1, -2)

    def test_Square_y_raise_value_error(self):
        with self.assertRaises(ValueError):
            Square(1, 2, -3)

    def test_Square_size_raise_value_error_2(self):
        with self.assertRaises(ValueError):
            Square(0)

    def test_Square_representation(self):
        square_repr = str(Square(1, 2, 3, 4))
        result = '[Square] (4) 2/3 - 1'
        self.assertEqual(square_repr, result)

    def test_Square_to_dictionary_exists(self):
        square_dict = Square(1, 2, 3, 4).to_dictionary()
        result = {
            'size': 1,
            'x': 2,
            'y': 3,
            'id': 4
        }
        self.assertEqual(square_dict, result)

    def test_Square_update_exists_1(self):
        square = Square(4, 3, 2, 1)
        square.update(89)
        self.assertEqual(square.id, 89)

    def test_Square_update_exists_2(self):
        square = Square(4, 3, 2, 1)
        square.update(89, 1)
        self.assertEqual(square.id, 89)
        self.assertEqual(square.size, 1)

    def test_Square_update_exists_3(self):
        square = Square(4, 3, 2, 1)
        square.update(89, 1, 2)
        self.assertEqual(square.id, 89)
        self.assertEqual(square.size, 1)
        self.assertEqual(square.x, 2)

    def test_Square_update_exists_4(self):
        square = Square(4, 3, 2, 1)
        square.update(89, 1, 2, 3)
        self.assertEqual(square.id, 89)
        self.assertEqual(square.size, 1)
        self.assertEqual(square.x, 2)
        self.assertEqual(square.y, 3)

    def test_Square_update_exists_6(self):
        square = Square(4, 3, 2, 1)
        square.update(**{'id': 89})
        self.assertEqual(square.id, 89)

    def test_Square_update_exists_7(self):
        square = Square(4, 3, 2, 1)
        square.update(**{'id': 89, 'size': 1})
        self.assertEqual(square.id, 89)
        self.assertEqual(square.size, 1)

    def test_Square_update_exists_8(self):
        square = Square(4, 3, 2, 1)
        square.update(**{'id': 89, 'size': 1, 'x': 2})
        self.assertEqual(square.id, 89)
        self.assertEqual(square.size, 1)
        self.assertEqual(square.x, 2)

    def test_Square_update_exists_9(self):
        square = Square(4, 3, 2, 1)
        square.update(**{'id': 89, 'size': 1, 'x': 2, 'y': 3})
        self.assertEqual(square.id, 89)
        self.assertEqual(square.size, 1)
        self.assertEqual(square.x, 2)
        self.assertEqual(square.y, 3)

    def test_Square_create_exists_1(self):
        with self.assertRaises(TypeError):
            Square.create(**{'id': 89})

    def test_Square_create_exists_2(self):
        square = Square.create(**{'id': 89, 'size': 1})
        self.assertEqual(square.id, 89)
        self.assertEqual(square.size, 1)

    def test_Square_create_exists_3(self):
        square = Square.create(**{'id': 89, 'size': 1, 'x': 2})
        self.assertEqual(square.id, 89)
        self.assertEqual(square.size, 1)
        self.assertEqual(square.x, 2)

    def test_Square_create_exists_4(self):
        square = Square.create(**{'id': 89, 'size': 1, 'x': 2, 'y': 3})
        self.assertEqual(square.id, 89)
        self.assertEqual(square.size, 1)
        self.assertEqual(square.x, 2)
        self.assertEqual(square.y, 3)

    def test_Square_save_to_file_exists_none(self):
        Square.save_to_file(None)

        with open('Square.json', 'r') as f:
            self.assertEqual(f.read(), '[]')

    def test_Square_save_to_file_exists_empty(self):
        Square.save_to_file([])

        with open('Square.json', 'r') as f:
            self.assertEqual(f.read(), '[]')

    def test_Square_save_to_file_exists(self):
        Square.save_to_file([Square(1)])

        with open('Square.json', 'r') as f:
            self.assertEqual(
                f.read(), '[{"id": 24, "size": 1, "x": 0, "y": 0}]')

    def test_Square_load_from_file_not_exists(self):
        self.assertEqual(Square.load_from_file(), [])