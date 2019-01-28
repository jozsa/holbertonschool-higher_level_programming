#!/usr/bin/python3
"""Unittest for class Rectangle
"""
import unittest
import io
from contextlib import redirect_stdout
from models.base import Base
from models.rectangle import Rectangle

class TestRectangleArgs(unittest.TestCase):
    """
    Instantation of Rectangle requires two to five arguments.
    1st argument: width
    2nd argument: height
    3rd argument: x
    4th argument: y
    5th argument: id
    """
    def setUp(self):
        Base.reset_nb_objects()

    def test_no_args(self):
        with self.assertRaises(TypeError):
            r1 = Rectangle()

    def test_one_arg(self):
        with self.assertRaises(TypeError):
            r1 = Rectangle(1)

    def test_two_args(self):
        r1 = Rectangle(4, 2)
        self.assertEqual(r1.width, 4)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)
        self.assertEqual(r1.id, 1)

    def test_three_args(self):
        r1 = Rectangle(6, 6, 6)
        self.assertEqual(r1.width, 6)
        self.assertEqual(r1.height, 6)
        self.assertEqual(r1.x, 6)
        self.assertEqual(r1.y, 0)
        self.assertEqual(r1.id, 1)

    def test_four_args(self):
        r1 = Rectangle(4, 2, 4, 2)
        self.assertEqual(r1.width, 4)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 4)
        self.assertEqual(r1.y, 2)
        self.assertEqual(r1.id, 1)

    def test_rect_init_with_all_args(self):
        r1 = Rectangle(4, 2, 7, 1, 42)
        self.assertEqual(r1.width, 4)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 7)
        self.assertEqual(r1.y, 1)
        self.assertEqual(r1.id, 42)

    def test_too_many_args(self):
        with self.assertRaises(TypeError):
            Rectangle(4, 5, 6, 7, 8, 9)

class TestRectangleSubClass(unittest.TestCase):
    def test_subclass(self):
        self.assertEqual(issubclass(Rectangle, Base), True)

class TestArgValidation(unittest.TestCase):
    def test_string_width(self):
        with self.assertRaises(TypeError):
            Rectangle("lol", 4)

    def test_string_height(self):
        with self.assertRaises(TypeError):
            Rectangle(4, "lol")

    def test_string_x(self):
        with self.assertRaises(TypeError):
            Rectangle(4, 4, "lol", 4)

    def test_string_y(self):
        with self.assertRaises(TypeError):
            Rectangle(4, 4, 4, "lol")

    def test_negative_width(self):
        with self.assertRaises(ValueError):
            Rectangle(-4, 4)

    def test_negative_height(self):
        with self.assertRaises(ValueError):
            Rectangle(4, -4)

    def test_negative_x(self):
        with self.assertRaises(ValueError):
            Rectangle(6, 6, -6, 6)

    def test_negative_y(self):
        with self.assertRaises(ValueError):
            Rectangle(6, 6, 6, -6)

class TestArea(unittest.TestCase):
    def setUp(self):
        Base.reset_nb_objects()

    def test_normal_area(self):
        r1 = Rectangle(4, 2)
        self.assertEqual(r1.area(), 8)

    def test_area_multiple_args(self):
        r1 = Rectangle(10, 2, 0, 0, 42)
        self.assertEqual(r1.area(), 20)

    def test_wrong_area(self):
        r1 = Rectangle(2, 2)
        with self.assertRaises(TypeError):
            r1.area(4)

class TestDisplay(unittest.TestCase):
    def setUp(self):
        Base.reset_nb_objects()

    def test_display(self):
        r1 = Rectangle(2, 2)
        with io.StringIO() as f, redirect_stdout(f):
            r1.display()
            s = f.getvalue()
        self.assertEqual(s, '##\n##\n')

    def test_display_with_axes(self):
        r1 = Rectangle(4, 4, 3, 3)
        with io.StringIO() as f, redirect_stdout(f):
            r1.display()
            s = f.getvalue()
        self.assertEqual(s, '\n\n\n   ####\n   ####\n   ####\n   ####\n')

    def test_display_with_arg(self):
        r1 = Rectangle(3, 2)
        with self.assertRaises(TypeError):
            r1.display(2)

class TestStrOverride(unittest.TestCase):
    def setUp(self):
        Base.reset_nb_objects()

    def test_str_all_args(self):
        r1 = Rectangle(4, 2, 4, 2, 4)
        self.assertEqual(r1.__str__(), '[Rectangle] (4) 4/2 - 4/2')

    def test_str_two_args(self):
        r1 = Rectangle(4, 2)
        self.assertEqual(r1.__str__(), '[Rectangle] (1) 0/0 - 4/2')

    def test_str_three_args(self):
        r1 = Rectangle(4, 2, 2)
        self.assertEqual(r1.__str__(), '[Rectangle] (1) 2/0 - 4/2')

    def test_str_four_args(self):
        r1 = Rectangle(7, 1, 7, 1)
        self.assertEqual(r1.__str__(), '[Rectangle] (1) 7/1 - 7/1')

    def test_invalid_str(self):
        r1 = Rectangle(1, 2)
        with self.assertRaises(TypeError):
            r1.__str__(2)

class TestUpdateArgsRectangle(unittest.TestCase):
    def setUp(self):
        Base.reset_nb_objects()
        self.r1 = Rectangle(4, 2, 4, 2, 4)

    def tearDown(self):
        del self.r1

    def test_update_all(self):
        self.r1.update(7, 1, 5, 2, 22)
        self.assertEqual(self.r1.id, 7)
        self.assertEqual(self.r1.width, 1)
        self.assertEqual(self.r1.height, 5)
        self.assertEqual(self.r1.x, 2)
        self.assertEqual(self.r1.y, 22)

    def test_update_id(self):
        self.r1.update(42)
        self.assertEqual(self.r1.id, 42)

    def test_update_width(self):
        self.r1.update(42, 42)
        self.assertEqual(self.r1.width, 42)

    def test_update_height(self):
        self.r1.update(42, 42, 42)
        self.assertEqual(self.r1.height, 42)

    def test_update_x(self):
        self.r1.update(42, 42, 42, 42)
        self.assertEqual(self.r1.x, 42)

    def test_update_y(self):
        self.r1.update(42, 42, 42, 42, 42)
        self.assertEqual(self.r1.y, 42)

    def test_invalid_update_width(self):
        with self.assertRaises(TypeError):
            self.r1.update(1, 'cat')

    def test_invalid_update_height(self):
        with self.assertRaises(TypeError):
            self.r1.update(1, 1, 'cat')

    def test_invalid_update_x(self):
        with self.assertRaises(TypeError):
            self.r1.update(1, 1, 1, 'cat')

    def test_invalid_update_y(self):
        with self.assertRaises(TypeError):
            self.r1.update(1, 1, 1, 1, 'cat')

    @unittest.expectedFailure
    def test_update_too_many_args(self):
        with self.assertRaises(TypeError):
            self.r1.update(4, 4, 4, 2, 2, 2)

    @unittest.expectedFailure
    def test_update_no_args(self):
        with self.assertRaises(TypeError):
            self.r1.update()

class TestUpdateKwargsRectangle(unittest.TestCase):
    def setUp(self):
        Base.reset_nb_objects()
        self.r1 = Rectangle(1, 1, 1, 1, 1)

    def tearDown(self):
        del self.r1

    def test_update_kid(self):
        self.r1.update(id=666)
        self.assertEqual(self.r1.id, 666)

    def test_update_kwidth(self):
        self.r1.update(width=666)
        self.assertEqual(self.r1.width, 666)

    def test_update_kheight(self):
        self.r1.update(height=666)
        self.assertEqual(self.r1.height, 666)

    def test_update_kx(self):
        self.r1.update(x=666)
        self.assertEqual(self.r1.x, 666)

    def test_update_ky(self):
        self.r1.update(y=666)
        self.assertEqual(self.r1.y, 666)

    def test_update_two_kwargs(self):
        self.r1.update(y=710, height=89)
        self.assertEqual(self.r1.y, 710)
        self.assertEqual(self.r1.height, 89)

    def test_update_three_kwargs(self):
        self.r1.update(width=3, id=89, x=42)
        self.assertEqual(self.r1.width, 3)
        self.assertEqual(self.r1.id, 89)
        self.assertEqual(self.r1.x, 42)

    def test_update_four_kwargs(self):
        self.r1.update(height=9, width=2, id=666, x=0)
        self.assertEqual(self.r1.height, 9)
        self.assertEqual(self.r1.width, 2)
        self.assertEqual(self.r1.id, 666)
        self.assertEqual(self.r1.x, 0)

    def test_both_args_kwargs(self):
        """
        If both args and kwargs are passed, kwargs should be ignored.
        """
        self.r1.update(2, 2, id=9)
        self.assertEqual(self.r1.id, 2)
        self.assertEqual(self.r1.width, 2)

    @unittest.expectedFailure
    def test_invalid_kwargs(self):
        self.r1.update(cat=42)
        self.assertEqual(self.r1.cat, 42)

    @unittest.expectedFailure
    def test_invalid_kwargs_in_valid_kwargs(self):
        self.r1.update(y=2, cat=42, width=9)
        self.assertEqual(self.r1.cat, 42)

    def test_invalid_kwargs_in_valid_kwargs_pass(self):
        self.r1.update(y=2, cat=42, width=9)
        self.assertEqual(self.r1.y, 2)
        self.assertEqual(self.r1.width, 9)

    def test_valid_keyword_invalid_arg(self):
        with self.assertRaises(TypeError):
            self.r1.update(y=[4, 5])

class TestToDictionary(unittest.TestCase):
    def setUp(self):
        Base.reset_nb_objects()
        self.r1 = Rectangle(4, 3, 2, 9, 710)
        self.r1_dict = self.r1.to_dictionary()

    def tearDown(self):
        del self.r1

    def test_return_type(self):
        self.assertEqual(type(self.r1_dict), dict)

    def test_to_dictionary(self):
        self.assertEqual(self.r1_dict, {'x': 2, 'y': 9, 'id': 710, 'height': 3, 'width': 4})

    def test_update_to_dictionary(self):
        self.r1.update(id=42)
        r1_dict = self.r1.to_dictionary()
        self.assertEqual(r1_dict, {'x': 2, 'y': 9, 'id': 42, 'height': 3, 'width': 4})

    def test_same_attrs_diff_obj(self):
        r2 = Rectangle(3, 4)
        r2.update(**self.r1_dict)
        self.assertIsNot(self.r1, r2)
