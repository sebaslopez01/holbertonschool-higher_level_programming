#!/usr/bin/python3

"""

This module defines test classes

"""

from io import StringIO
import unittest
import os
from unittest.mock import patch
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
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


class TestRectangle(unittest.TestCase):
    def test_rectangle_creation_1(self):
        rect = Rectangle(1, 2)
        self.assertEqual(rect.width, 1)
        self.assertEqual(rect.height, 2)

    def test_rectangle_creation_2(self):
        rect = Rectangle(1, 2, 3)
        self.assertEqual(rect.width, 1)
        self.assertEqual(rect.height, 2)
        self.assertEqual(rect.x, 3)

    def test_rectangle_creation_3(self):
        rect = Rectangle(1, 2, 3, 4)
        self.assertEqual(rect.width, 1)
        self.assertEqual(rect.height, 2)
        self.assertEqual(rect.x, 3)
        self.assertEqual(rect.y, 4)

    def test_rectangle_width_raise_type_error(self):
        with self.assertRaises(TypeError):
            Rectangle("1", 2)

    def test_rectangle_height_raise_type_error(self):
        with self.assertRaises(TypeError):
            Rectangle(1, "2")

    def test_rectangle_x_raise_type_error(self):
        with self.assertRaises(TypeError):
            Rectangle(1, 2, "3")

    def test_rectangle_y_raise_type_error(self):
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, "4")

    def test_rectangle_creation_4(self):
        rect = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(rect.width, 1)
        self.assertEqual(rect.height, 2)
        self.assertEqual(rect.x, 3)
        self.assertEqual(rect.y, 4)
        self.assertEqual(rect.id, 5)

    def test_rectangle_width_raise_value_error(self):
        with self.assertRaises(ValueError):
            Rectangle(-1, 2)

    def test_rectangle_height_raise_value_error(self):
        with self.assertRaises(ValueError):
            Rectangle(1, -2)

    def test_rectangle_width_raise_value_error_2(self):
        with self.assertRaises(ValueError):
            Rectangle(0, 2)

    def test_rectangle_height_raise_value_error_2(self):
        with self.assertRaises(ValueError):
            Rectangle(1, 0)

    def test_rectangle_x_raise_value_error(self):
        with self.assertRaises(ValueError):
            Rectangle(1, 2, -3)

    def test_rectangle_y_raise_value_error(self):
        with self.assertRaises(ValueError):
            Rectangle(1, 2, 3, -4)

    def test_rectangle_area(self):
        self.assertEqual(Rectangle(2, 2).area(), 4)

    def test_rectangle_representation(self):
        rect_repr = str(Rectangle(1, 2, 3, 4, 5))
        result = '[Rectangle] (5) 3/4 - 1/2'
        self.assertEqual(rect_repr, result)

    def test_rectangle_display_without_x_and_y(self):
        with patch('sys.stdout', new=StringIO()) as out:
            Rectangle(2, 2).display()
            self.assertEqual(out.getvalue(), '##\n##\n')

    def test_rectangle_display_without_y(self):
        with patch('sys.stdout', new=StringIO()) as out:
            Rectangle(2, 2, 1).display()
            self.assertEqual(out.getvalue(), ' ##\n ##\n')

    def test_rectangle_display_exists(self):
        with patch('sys.stdout', new=StringIO()) as out:
            Rectangle(2, 2, 1, 1).display()
            self.assertEqual(out.getvalue(), '\n ##\n ##\n')

    def test_rectangle_to_dictionary_exists(self):
        rect_dict = Rectangle(1, 2, 3, 4, 5).to_dictionary()
        result = {
            'width': 1,
            'height': 2,
            'x': 3,
            'y': 4,
            'id': 5
        }
        self.assertEqual(rect_dict, result)

    def test_rectangle_update_exists_1(self):
        rect = Rectangle(5, 4, 3, 2, 1)
        rect.update(89)
        self.assertEqual(rect.id, 89)

    def test_rectangle_update_exists_2(self):
        rect = Rectangle(5, 4, 3, 2, 1)
        rect.update(89, 1)
        self.assertEqual(rect.id, 89)
        self.assertEqual(rect.width, 1)

    def test_rectangle_update_exists_3(self):
        rect = Rectangle(5, 4, 3, 2, 1)
        rect.update(89, 1, 2)
        self.assertEqual(rect.id, 89)
        self.assertEqual(rect.width, 1)
        self.assertEqual(rect.height, 2)

    def test_rectangle_update_exists_4(self):
        rect = Rectangle(5, 4, 3, 2, 1)
        rect.update(89, 1, 2, 3)
        self.assertEqual(rect.id, 89)
        self.assertEqual(rect.width, 1)
        self.assertEqual(rect.height, 2)
        self.assertEqual(rect.x, 3)

    def test_rectangle_update_exists_5(self):
        rect = Rectangle(5, 4, 3, 2, 1)
        rect.update(89, 1, 2, 3, 4)
        self.assertEqual(rect.id, 89)
        self.assertEqual(rect.width, 1)
        self.assertEqual(rect.height, 2)
        self.assertEqual(rect.x, 3)
        self.assertEqual(rect.y, 4)

    def test_rectangle_update_exists_6(self):
        rect = Rectangle(5, 4, 3, 2, 1)
        rect.update(**{'id': 89})
        self.assertEqual(rect.id, 89)

    def test_rectangle_update_exists_7(self):
        rect = Rectangle(5, 4, 3, 2, 1)
        rect.update(**{'id': 89, 'width': 1})
        self.assertEqual(rect.id, 89)
        self.assertEqual(rect.width, 1)

    def test_rectangle_update_exists_8(self):
        rect = Rectangle(5, 4, 3, 2, 1)
        rect.update(**{'id': 89, 'width': 1, 'height': 2})
        self.assertEqual(rect.id, 89)
        self.assertEqual(rect.width, 1)
        self.assertEqual(rect.height, 2)

    def test_rectangle_update_exists_9(self):
        rect = Rectangle(5, 4, 3, 2, 1)
        rect.update(**{'id': 89, 'width': 1, 'height': 2, 'x': 3})
        self.assertEqual(rect.id, 89)
        self.assertEqual(rect.width, 1)
        self.assertEqual(rect.height, 2)
        self.assertEqual(rect.x, 3)

    def test_rectangle_update_exists_10(self):
        rect = Rectangle(5, 4, 3, 2, 1)
        rect.update(**{'id': 89, 'width': 1, 'height': 2, 'x': 3, 'y': 4})
        self.assertEqual(rect.id, 89)
        self.assertEqual(rect.width, 1)
        self.assertEqual(rect.height, 2)
        self.assertEqual(rect.x, 3)
        self.assertEqual(rect.y, 4)

    def test_rectangle_create_exists_1(self):
        with self.assertRaises(TypeError):
            Rectangle.create(**{'id': 89})

    def test_rectangle_create_exists_2(self):
        with self.assertRaises(TypeError):
            Rectangle.create(**{'id': 89, 'width': 1})

    def test_rectangle_create_exists_3(self):
        rect = Rectangle.create(**{'id': 89, 'width': 1, 'height': 2})
        self.assertEqual(rect.id, 89)
        self.assertEqual(rect.width, 1)
        self.assertEqual(rect.height, 2)

    def test_rectangle_create_exists_4(self):
        rect = Rectangle.create(**{'id': 89, 'width': 1, 'height': 2, 'x': 3})
        self.assertEqual(rect.id, 89)
        self.assertEqual(rect.width, 1)
        self.assertEqual(rect.height, 2)
        self.assertEqual(rect.x, 3)

    def test_rectangle_create_exists_5(self):
        rect = Rectangle.create(**{
            'id': 89,
            'width': 1,
            'height': 2,
            'x': 3,
            'y': 4
        })
        self.assertEqual(rect.id, 89)
        self.assertEqual(rect.width, 1)
        self.assertEqual(rect.height, 2)
        self.assertEqual(rect.x, 3)
        self.assertEqual(rect.y, 4)

    def test_rectangle_save_to_file_exists_none(self):
        Rectangle.save_to_file(None)

        with open('Rectangle.json', 'r') as f:
            self.assertEqual(f.read(), '[]')
        os.remove('Rectangle.json')

    def test_rectangle_save_to_file_exists_empty(self):
        Rectangle.save_to_file([])

        with open('Rectangle.json', 'r') as f:
            self.assertEqual(f.read(), '[]')
        os.remove('Rectangle.json')

    def test_rectangle_save_to_file_exists(self):
        Rectangle.save_to_file([Rectangle(1, 2)])

        with open('Rectangle.json', 'r') as f:
            self.assertEqual(
                f.read(), '[{"id": 13, "width": 1, "height": 2, "x": 0, "y": 0}]')

    # def test_rectangle_load_from_file_not_exists(self):
    #     Rectangle.save_to_file([])
    #     self.assertEqual(Rectangle.load_from_file(), [])

    # def test_rectangle_load_from_file_exists(self):
    #     Rectangle.save_to_file([Rectangle(1, 2, 1, 1, 5)])
    #     lst_obj = Rectangle.load_from_file()

    #     self.assertEqual(lst_obj[0].width, 1)


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

    # def test_Square_save_to_file_exists_none(self):
    #     Square.save_to_file(None)

    #     with open('Square.json', 'r') as f:
    #         self.assertEqual(f.read(), '[]')

    # def test_Square_save_to_file_exists_empty(self):
    #     Square.save_to_file([])

    #     with open('Square.json', 'r') as f:
    #         self.assertEqual(f.read(), '[]')

    # def test_Square_save_to_file_exists(self):
    #     Square.save_to_file([Square(1)])

    #     with open('Square.json', 'r') as f:
    #         self.assertEqual(
    #             f.read(), '[{"id": 24, "size": 1, "x": 0, "y": 0}]')

    # def test_Square_load_from_file_not_exists(self):
    #     Square.save_to_file([])
    #     self.assertEqual(Square.load_from_file(), [])

    # def test_rectangle_load_from_file_exists(self):
    #     Square.save_to_file([Square(1, 1, 1, 5)])
    #     lst_obj = Square.load_from_file()

    #     self.assertEqual(lst_obj[0].size, 1)
