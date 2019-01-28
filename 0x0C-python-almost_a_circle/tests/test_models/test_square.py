#!/usr/bin/python3
"""Unittest for class Square
"""
import unittest
import io
from contextlib import redirect_stdout
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

class TestSquareArgs(unittest.TestCase):
    """
    Instantation of Square requires one to four arguments.
    1st argument: size
    2nd argument: x
    3rd argument: y
    4th argument: id
    """
    def setUp(self):
        Base.reset_nb_objects()

    def test_no_args(self):
        with self.assertRaises(TypeError):
            s1 = Square()

    def test_one_arg(self):
        s1 = Square(42)
        self.assertEqual(s1.size, 42)
        self.assertEqual(s1.x, 0)
        self.assertEqual(s1.y, 0)
        self.assertEqual(s1.id, 1)

    def test_two_args(self):
        s1 = Square(2, 3)
        self.assertEqual(s1.size, 2)
        self.assertEqual(s1.x, 3)
        self.assertEqual(s1.y, 0)
        self.assertEqual(s1.id, 1)

    def test_three_args(self):
        s1 = Square(6, 6, 6)
        self.assertEqual(s1.size, 6)
        self.assertEqual(s1.x, 6)
        self.assertEqual(s1.y, 6)
        self.assertEqual(s1.id, 1)

    def test_four_args(self):
        s1 = Square(6, 6, 6, 6)
        self.assertEqual(s1.size, 6)
        self.assertEqual(s1.x, 6)
        self.assertEqual(s1.y, 6)
        self.assertEqual(s1.id, 6)

    def test_too_many_args(self):
        with self.assertRaises(TypeError):
            Square(6, 6, 6, 6, 6)

    def test_equality(self):
        s1 = Square(4)
        self.assertEqual(s1.size == s1.width, True)
        self.assertEqual(s1.size == s1.height, True)

class TestSquareSubClass(unittest.TestCase):
    def test_subclass(self):
        self.assertEqual(issubclass(Square, Rectangle), True)

class TestArgValidation(unittest.TestCase):
    def test_string_size(self):
        with self.assertRaises(TypeError):
            Square('ha')

    def test_tuple_x(self):
        with self.assertRaises(TypeError):
            Square(1, (4, 5))

    def test_list_y(self):
        with self.assertRaises(TypeError):
            Square(1, 4, [5, 6])

    def test_zero_size(self):
        with self.assertRaises(ValueError):
            Square(0)

    def test_negative_x(self):
        with self.assertRaises(ValueError):
            Square(3, -3)

    def test_negative_y(self):
        with self.assertRaises(ValueError):
            Square(3, 3, -3)

class TestArea(unittest.TestCase):
    def setUp(self):
        Base.reset_nb_objects()

    def test_normal_area(self):
        s1 = Square(4)
        self.assertEqual(s1.area(), 16)

    def test_area_multiple_args(self):
        s1 = Square(4, 1, 3, 2)
        self.assertEqual(s1.area(), 16)

class TestDisplay(unittest.TestCase):
    def setUp(self):
        Base.reset_nb_objects()

    def test_display(self):
        s1 = Square(2)
        with io.StringIO() as f, redirect_stdout(f):
            s1.display()
            s = f.getvalue()
        self.assertEqual(s, '##\n##\n')

    def test_display_with_axes(self):
        s1 = Square(3, 3, 3)
        with io.StringIO() as f, redirect_stdout(f):
            s1.display()
            s = f.getvalue()
        self.assertEqual(s, '\n\n\n   ###\n   ###\n   ###\n')

    def test_display_with_arg(self):
        s1 = Square(3)
        with self.assertRaises(TypeError):
            s1.display(3)

class TestStrOverride(unittest.TestCase):
    def setUp(self):
        Base.reset_nb_objects()

    def test_str_all_args(self):
        s1 = Square(4, 2, 4, 2)
        self.assertEqual(s1.__str__(), '[Square] (2) 2/4 - 4')

    def test_str_one_arg(self):
        s1 = Square(4)
        self.assertEqual(s1.__str__(), '[Square] (1) 0/0 - 4')

    def test_str_two_args(self):
        s1 = Square(4, 2)
        self.assertEqual(s1.__str__(), '[Square] (1) 2/0 - 4')

    def test_str_three_args(self):
        s1 = Square(4, 2, 5)
        self.assertEqual(s1.__str__(), '[Square] (1) 2/5 - 4')

    def test_str_four_args(self):
        s1 = Square(4, 2, 5, 42)
        self.assertEqual(s1.__str__(), '[Square] (42) 2/5 - 4')

    def test_invalid_str(self):
        s1 = Square(3)
        with self.assertRaises(TypeError):
            s1.__str__(2)


class TestUpdateArgsSquare(unittest.TestCase):
    def setUp(self):
        Base.reset_nb_objects()
        self.s1 = Square(4, 4, 4, 4)

    def tearDown(self):
        del self.s1

    def test_update_all(self):
        self.s1.update(42, 3, 2, 2)
        self.assertEqual(self.s1.id, 42)
        self.assertEqual(self.s1.size, 3)
        self.assertEqual(self.s1.x, 2)
        self.assertEqual(self.s1.y, 2)

    def test_update_id(self):
        self.s1.update(42)
        self.assertEqual(self.s1.id, 42)

    def test_update_size(self):
        self.s1.update(0, 5)
        self.assertEqual(self.s1.size, 5)

    def test_update_x(self):
        self.s1.update(0, 2, 2)
        self.assertEqual(self.s1.x, 2)

    def test_update_y(self):
        self.s1.update(0, 3, 3, 3)
        self.assertEqual(self.s1.y, 3)

    def test_invalid_update_size(self):
        with self.assertRaises(TypeError):
            self.s1.update(1, 'cat')

    def test_invalid_update_x(self):
        with self.assertRaises(TypeError):
            self.s1.update(1, 1, 'cat')

    def test_invalid_update_x(self):
        with self.assertRaises(TypeError):
            self.s1.update(1, 1, 1, 'cat')

    @unittest.expectedFailure
    def test_update_too_many_args(self):
        with self.assertRaises(TypeError):
            self.s1.update(4, 4, 4, 2, 2)

    @unittest.expectedFailure
    def test_update_no_args(self):
        with self.assertRaises(TypeError):
            self.s1.update()

class TestUpdateKwargsSquare(unittest.TestCase):
    def setUp(self):
        Base.reset_nb_objects()
        self.s1 = Square(42, 42, 42, 42)

    def tearDown(self):
        del self.s1

    def test_update_kid(self):
        self.s1.update(id=710)
        self.assertEqual(self.s1.id, 710)

    def test_update_ksize(self):
        self.s1.update(size=4)
        self.assertEqual(self.s1.size, 4)

    def test_update_kx(self):
        self.s1.update(x=2)
        self.assertEqual(self.s1.x, 2)

    def test_update_ky(self):
        self.s1.update(y=2)
        self.assertEqual(self.s1.y, 2)

    def test_update_two_kwargs(self):
        self.s1.update(y=2, id=666)
        self.assertEqual(self.s1.y, 2)
        self.assertEqual(self.s1.id, 666)

    def test_update_three_kwargs(self):
        self.s1.update(x=0, y=0, id=6)
        self.assertEqual(self.s1.x, 0)
        self.assertEqual(self.s1.y, 0)
        self.assertEqual(self.s1.id, 6)

    def test_both_args_kwargs(self):
        """
        If both args and kwargs are passed, kwargs should be ignored.
        """
        self.s1.update(4, 3, y=9)
        self.assertEqual(self.s1.id, 4)
        self.assertEqual(self.s1.size, 3)
        self.assertEqual(self.s1.y, 42)

    @unittest.expectedFailure
    def test_invalid_kwargs(self):
        self.s1.update(cat=42)
        self.assertEqual(self.s1.cat, 42)

    @unittest.expectedFailure
    def test_invalid_kwargs_in_valid_kwargs(self):
        self.s1.update(x=2, cat=42, id=90)
        self.assertEqual(self.s1.cat, 42)

    def valid_keyword_invalid_arg(self):
        with self.assertRaises(TypeError):
            self.s1.update(x=[6, 6])

class TestToDictionary(unittest.TestCase):
    def setUp(self):
        Base.reset_nb_objects()
        self.s1 = Square(4, 2, 9, 710)
        self.s1_dict = self.s1.to_dictionary()

    def tearDown(self):
        del self.s1

    def test_return_type(self):
        self.assertEqual(type(self.s1_dict), dict)

    def test_to_dictionary(self):
        self.assertEqual(self.s1_dict, {'x': 2, 'y': 9, 'id': 710, 'size': 4})

    def test_update_to_dictionary(self):
        self.s1.update(id=42)
        s1_dict = self.s1.to_dictionary()
        self.assertEqual(s1_dict, {'x': 2, 'y': 9, 'id': 42, 'size': 4})

    def test_same_attrs_diff_obj(self):
        s2 = Square(3)
        s2.update(**self.s1_dict)
        self.assertIsNot(self.s1, s2)
