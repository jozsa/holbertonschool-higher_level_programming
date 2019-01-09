#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_small_listint(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_inf(self):
        self.assertEqual(max_integer([float('inf'),
                         float('-inf')]), float('inf'))

    def test_lowest_nbr(self):
        self.assertEqual(max_integer([float('-inf'), 0]), 0)

    def test_args(self):
        with self.assertRaises(TypeError):
            max_integer(4, 2)

    def test_float(self):
        self.assertEqual(max_integer([4.5, 4.2]), 4.5)

    def test_strings(self):
        self.assertEqual(max_integer(['long', 'short']), 'short')

    def test_string(self):
        self.assertEqual(max_integer('lol'), 'o')
