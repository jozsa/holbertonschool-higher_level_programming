#!/usr/bin/python3
"""Unittest for class Base
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import os


class TestBaseIdOrder(unittest.TestCase):
    def setUp(self):
        Base.reset_nb_objects()

    def test_id(self):
        b1 = Base(1)
        b2 = Base()
        self.assertEqual(b2.id, 1)
        self.assertEqual(b1.id, 1)

    def test_id_order(self):
        b1 = Base()
        b2 = Base()
        b3 = Base()
        b4 = Base()
        b5 = Base()
        self.assertEqual(b5.id, 5)

    def test_str_id(self):
        b1 = Base('hi')
        self.assertEqual(b1.id, 'hi')

    def test_list_id(self):
        b1 = Base([4, 2])
        self.assertEqual(b1.id, [4, 2])

    def test_tuple_id(self):
        b1 = Base((1, 2))
        self.assertEqual(b1.id, (1, 2))

    def test_two_args(self):
        with self.assertRaises(TypeError):
            b1 = Base(1, 2)

    def test_no_args(self):
        b1 = Base()
        self.assertEqual(b1.id, 1)

    def test_one_arg(self):
        b1 = Base(42)
        self.assertEqual(b1.id, 42)


class TestToJsonString(unittest.TestCase):
    def test_empty_list(self):
        r = Base.to_json_string(None)
        self.assertEqual(r, "[]")

    def test_none(self):
        r = Base.to_json_string([])
        self.assertEqual(r, "[]")

    def test_two_dicts(self):
        r = Base.to_json_string([{"y": 8, "x": 2, "id": 1,
                                  "width": 10, "height": 7},
                                 {"y": 0, "x": 0, "id": 2,
                                  "width": 2, "height": 4}])
        self.assertEqual(type(r), str)


class TestSaveToFile(unittest.TestCase):
    def test_none(self):
        Rectangle.save_to_file([])
        with open('Rectangle.json', 'r') as a_file:
            length = len(a_file.read())
        self.assertEqual(length, 2)

    def test_one_instance(self):
        r1 = Rectangle(3, 4, 9, 0, 42)
        Rectangle.save_to_file([r1])
        with open('Rectangle.json', 'r') as a_file:
            length = len(a_file.read())
        self.assertEqual(length, 53)

    def test_two_instances(self):
        r1 = Rectangle(42, 42, 42, 42, 42)
        r2 = Rectangle(710, 710, 710, 710, 710)
        Rectangle.save_to_file([r1, r2])
        with open('Rectangle.json', 'r') as a_file:
            length = len(a_file.read())
        self.assertEqual(length, 119)
