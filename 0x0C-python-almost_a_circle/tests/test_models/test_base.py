#!/usr/bin/python3
"""Unittest for class Base
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import os


class TestBase(unittest.TestCase):
    """Testing base"""
    def setUp(self):
        """
        Reset number of objects to 0 each time a test is run
        """
        Base.reset_nb_objects()

    def test_id(self):
        """
        Test that id gets set correctly
        """
        b1 = Base(1)
        b2 = Base()
        self.assertEqual(b2.id, 1)
        self.assertEqual(b1.id, 1)

    def test_id_order(self):
        """
        Test that id gets incremented correctly
        """
        b1 = Base()
        b2 = Base()
        b3 = Base()
        b4 = Base()
        b5 = Base()
        self.assertEqual(b5.id, 5)

    def test_str_id(self):
        """
        Test setting a string as the id
        """
        b1 = Base('hi')
        self.assertEqual(b1.id, 'hi')

    def test_list_id(self):
        """
        Test setting a list as the id
        """
        b1 = Base([4, 2])
        self.assertEqual(b1.id, [4, 2])

    def test_tuple_id(self):
        """
        Test setting a tuple as the id
        """
        b1 = Base((1, 2))
        self.assertEqual(b1.id, (1, 2))

    def test_two_args(self):
        """
        Test instantation of Base with two args
        """
        with self.assertRaises(TypeError):
            b1 = Base(1, 2)

    def test_no_args(self):
        """
        Instantation of Base with no args
        """
        b1 = Base()
        self.assertEqual(b1.id, 1)

    def test_one_arg(self):
        """
        Instantation of Base with one arg
        """
        b1 = Base(42)
        self.assertEqual(b1.id, 42)

    def test_to_json_none(self):
        """
        Test passing None to_json_string
        """
        r = Base.to_json_string(None)
        self.assertEqual(r, "[]")

    def test_none(self):
        """
        Test passing empty string to_json_string
        """
        r = Base.to_json_string([])
        self.assertEqual(r, "[]")

    def test_two_dicts(self):
        """
        Test passing list of two dicts to_json_string
        """
        r = Base.to_json_string([{"y": 8, "x": 2, "id": 1,
                                  "width": 10, "height": 7},
                                 {"y": 0, "x": 0, "id": 2,
                                  "width": 2, "height": 4}])
        self.assertEqual(type(r), str)

    def test_empty_list(self):
        """
        Test passing empty list to save_to_file
        """
        Rectangle.save_to_file([])
        with open('Rectangle.json', 'r') as a_file:
            length = len(a_file.read())
        self.assertEqual(length, 2)

    def test_one_instance(self):
        """
        Test passing list of one instance to save_to_file
        """
        r1 = Rectangle(3, 4, 9, 0, 42)
        Rectangle.save_to_file([r1])
        with open('Rectangle.json', 'r') as a_file:
            length = len(a_file.read())
        self.assertEqual(length, 53)

    def test_two_instances(self):
        """
        Test passing list of two instances to save_to_file
        """
        r1 = Rectangle(42, 42, 42, 42, 42)
        r2 = Rectangle(710, 710, 710, 710, 710)
        Rectangle.save_to_file([r1, r2])
        with open('Rectangle.json', 'r') as a_file:
            length = len(a_file.read())
        self.assertEqual(length, 119)
