#!/usr/bin/python3

"""

This module defines test classes

"""

import unittest
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

    def test_rectangle_display_without_x(self):
        self.assertEqual(Rectangle(1, 2, 0, 4).display(), None)

    def test_rectangle_display_without_y(self):
        self.assertEqual(Rectangle(1, 2, 3).display(), None)

    def test_rectangle_display_exists(self):
        self.assertEqual(Rectangle(1, 2, 3, 4).display(), None)

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

    def test_rectangle_save_to_file_exists_empty(self):
        Rectangle.save_to_file([])

        with open('Rectangle.json', 'r') as f:
            self.assertEqual(f.read(), '[]')

    def test_rectangle_save_to_file_exists(self):
        Rectangle.save_to_file([Rectangle(1, 2)])

        with open('Rectangle.json', 'r') as f:
            self.assertEqual(
                f.read(), '[{"id": 13, "width": 1, "height": 2, "x": 0, "y": 0}]')

    def test_rectangle_load_from_file_not_exists(self):
        self.assertEqual(Rectangle.load_from_file(), [])
