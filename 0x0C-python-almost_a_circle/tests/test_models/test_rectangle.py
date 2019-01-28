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
        """Reset number of objects to 0 before each test"""
        Base.reset_nb_objects()

    def test_no_args(self):
        """Instantiate Rectangle with no arguments"""
        with self.assertRaises(TypeError):
            r1 = Rectangle()

    def test_one_arg(self):
        """Instantiate Rectangle with one argument"""
        with self.assertRaises(TypeError):
            r1 = Rectangle(1)

    def test_two_args(self):
        """Instantiate Rectangle with two arguments"""
        r1 = Rectangle(4, 2)
        self.assertEqual(r1.width, 4)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)
        self.assertEqual(r1.id, 1)

    def test_three_args(self):
        """Instantiate Rectangle with three arguments"""
        r1 = Rectangle(6, 6, 6)
        self.assertEqual(r1.width, 6)
        self.assertEqual(r1.height, 6)
        self.assertEqual(r1.x, 6)
        self.assertEqual(r1.y, 0)
        self.assertEqual(r1.id, 1)

    def test_four_args(self):
        """Instantiate Rectangle with four arguments"""
        r1 = Rectangle(4, 2, 4, 2)
        self.assertEqual(r1.width, 4)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 4)
        self.assertEqual(r1.y, 2)
        self.assertEqual(r1.id, 1)

    def test_rect_init_with_all_args(self):
        """Instantiate Rectangle with all arguments"""
        r1 = Rectangle(4, 2, 7, 1, 42)
        self.assertEqual(r1.width, 4)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 7)
        self.assertEqual(r1.y, 1)
        self.assertEqual(r1.id, 42)

    def test_too_many_args(self):
        """Instantiate Rectangle with too many arguments"""
        with self.assertRaises(TypeError):
            Rectangle(4, 5, 6, 7, 8, 9)

    def test_subclass(self):
        """Test if Rectangle is subclass of Base"""
        self.assertEqual(issubclass(Rectangle, Base), True)


class TestArgValidation(unittest.TestCase):
    """Pass string as width"""
    def test_string_width(self):
        with self.assertRaises(TypeError):
            Rectangle("lol", 4)

    def test_string_height(self):
        """String as height"""
        with self.assertRaises(TypeError):
            Rectangle(4, "lol")

    def test_string_x(self):
        """String as x"""
        with self.assertRaises(TypeError):
            Rectangle(4, 4, "lol", 4)

    def test_string_y(self):
        """String as y"""
        with self.assertRaises(TypeError):
            Rectangle(4, 4, 4, "lol")

    def test_negative_width(self):
        """Negative number as width"""
        with self.assertRaises(ValueError):
            Rectangle(-4, 4)

    def test_negative_height(self):
        """Negative number as height"""
        with self.assertRaises(ValueError):
            Rectangle(4, -4)

    def test_negative_x(self):
        """Passing negative number as x"""
        with self.assertRaises(ValueError):
            Rectangle(6, 6, -6, 6)

    def test_negative_y(self):
        """Passing negative number as y"""
        with self.assertRaises(ValueError):
            Rectangle(6, 6, 6, -6)


class TestArea(unittest.TestCase):
    """Test area() class method"""
    def setUp(self):
        """Reset number of objects to 0 before each test"""
        Base.reset_nb_objects()

    def test_normal_area(self):
        """Test area with one argument instantation"""
        r1 = Rectangle(4, 2)
        self.assertEqual(r1.area(), 8)

    def test_area_multiple_args(self):
        """Test area with multiple args instantation"""
        r1 = Rectangle(10, 2, 0, 0, 42)
        self.assertEqual(r1.area(), 20)

    def test_wrong_area(self):
        """Test area with argument passed"""
        r1 = Rectangle(2, 2)
        with self.assertRaises(TypeError):
            r1.area(4)


class TestDisplay(unittest.TestCase):
    """Test display() class method"""
    def setUp(self):
        """Reset number of objects to 0 before each test"""
        Base.reset_nb_objects()

    def test_display(self):
        """Display 2 by 2 rectangle"""
        r1 = Rectangle(2, 2)
        with io.StringIO() as f, redirect_stdout(f):
            r1.display()
            s = f.getvalue()
        self.assertEqual(s, '##\n##\n')

    def test_display_with_axes(self):
        """Display 4 by 4 rectangle with offset of 3 for x/y axes"""
        r1 = Rectangle(4, 4, 3, 3)
        with io.StringIO() as f, redirect_stdout(f):
            r1.display()
            s = f.getvalue()
        self.assertEqual(s, '\n\n\n   ####\n   ####\n   ####\n   ####\n')

    def test_display_with_arg(self):
        """Display with an argument passed"""
        r1 = Rectangle(3, 2)
        with self.assertRaises(TypeError):
            r1.display(2)


class TestStrOverride(unittest.TestCase):
    """Test __str__ override for Square class"""
    def setUp(self):
        """Reset number of objects to 0 before each test"""
        Base.reset_nb_objects()

    def test_str_all_args(self):
        """Test __str__ with instantation with all arguments"""
        r1 = Rectangle(4, 2, 4, 2, 4)
        self.assertEqual(r1.__str__(), '[Rectangle] (4) 4/2 - 4/2')

    def test_str_two_args(self):
        """Test __str__ with instantation with two arguments"""
        r1 = Rectangle(4, 2)
        self.assertEqual(r1.__str__(), '[Rectangle] (1) 0/0 - 4/2')

    def test_str_three_args(self):
        """Test __str__ with instantation with three arguments"""
        r1 = Rectangle(4, 2, 2)
        self.assertEqual(r1.__str__(), '[Rectangle] (1) 2/0 - 4/2')

    def test_str_four_args(self):
        """Test __str__ with instantation with four arguments"""
        r1 = Rectangle(7, 1, 7, 1)
        self.assertEqual(r1.__str__(), '[Rectangle] (1) 7/1 - 7/1')

    def test_invalid_str(self):
        """Passing argument to __str__"""
        r1 = Rectangle(1, 2)
        with self.assertRaises(TypeError):
            r1.__str__(2)


class TestUpdateArgsRectangle(unittest.TestCase):
    """Test update() class method"""
    def setUp(self):
        """Instantiate object for use & reset number
        of objects to 0 before each test"""
        Base.reset_nb_objects()
        self.r1 = Rectangle(4, 2, 4, 2, 4)

    def tearDown(self):
        """Delete square instance"""
        del self.r1

    def test_update_all(self):
        """Update all attributes"""
        self.r1.update(7, 1, 5, 2, 22)
        self.assertEqual(self.r1.id, 7)
        self.assertEqual(self.r1.width, 1)
        self.assertEqual(self.r1.height, 5)
        self.assertEqual(self.r1.x, 2)
        self.assertEqual(self.r1.y, 22)

    def test_update_id(self):
        """Update only id"""
        self.r1.update(42)
        self.assertEqual(self.r1.id, 42)

    def test_update_width(self):
        """Update width and id"""
        self.r1.update(42, 42)
        self.assertEqual(self.r1.width, 42)

    def test_update_height(self):
        "Update height, width, and id"""
        self.r1.update(42, 42, 42)
        self.assertEqual(self.r1.height, 42)

    def test_update_x(self):
        """Update height, width, x, and id"""
        self.r1.update(42, 42, 42, 42)
        self.assertEqual(self.r1.x, 42)

    def test_update_y(self):
        """Update height, width, x, y, and id"""
        self.r1.update(42, 42, 42, 42, 42)
        self.assertEqual(self.r1.y, 42)

    def test_invalid_update_width(self):
        """Update with string passed as width"""
        with self.assertRaises(TypeError):
            self.r1.update(1, 'cat')

    def test_invalid_update_height(self):
        """Update with string passed as height"""
        with self.assertRaises(TypeError):
            self.r1.update(1, 1, 'cat')

    def test_invalid_update_x(self):
        """Update with string passed as x"""
        with self.assertRaises(TypeError):
            self.r1.update(1, 1, 1, 'cat')

    def test_invalid_update_y(self):
        """Update with string passed as y"""
        with self.assertRaises(TypeError):
            self.r1.update(1, 1, 1, 1, 'cat')

    @unittest.expectedFailure
    def test_update_too_many_args(self):
        """Update with too many args passed"""
        with self.assertRaises(TypeError):
            self.r1.update(4, 4, 4, 2, 2, 2)

    @unittest.expectedFailure
    def test_update_no_args(self):
        """Update with no arguments"""
        with self.assertRaises(TypeError):
            self.r1.update()


class TestUpdateKwargsRectangle(unittest.TestCase):
    """Test update using keyword arguments"""
    def setUp(self):
        """
        Instantiate new Square object for use and
        reset number of objects to 0 before each test
        """
        Base.reset_nb_objects()
        self.r1 = Rectangle(1, 1, 1, 1, 1)

    def tearDown(self):
        """Delete rectangle object"""
        del self.r1

    def test_update_kid(self):
        """Update id only"""
        self.r1.update(id=666)
        self.assertEqual(self.r1.id, 666)

    def test_update_kwidth(self):
        """Update width only"""
        self.r1.update(width=666)
        self.assertEqual(self.r1.width, 666)

    def test_update_kheight(self):
        """Update height only"""
        self.r1.update(height=666)
        self.assertEqual(self.r1.height, 666)

    def test_update_kx(self):
        """Update x only"""
        self.r1.update(x=666)
        self.assertEqual(self.r1.x, 666)

    def test_update_ky(self):
        """Update y only"""
        self.r1.update(y=666)
        self.assertEqual(self.r1.y, 666)

    def test_update_two_kwargs(self):
        """Update two keyword args"""
        self.r1.update(y=710, height=89)
        self.assertEqual(self.r1.y, 710)
        self.assertEqual(self.r1.height, 89)

    def test_update_three_kwargs(self):
        """Update three keyword args"""
        self.r1.update(width=3, id=89, x=42)
        self.assertEqual(self.r1.width, 3)
        self.assertEqual(self.r1.id, 89)
        self.assertEqual(self.r1.x, 42)

    def test_update_four_kwargs(self):
        """Update four keyword args"""
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
        """Test invalid keyword"""
        self.r1.update(cat=42)
        self.assertEqual(self.r1.cat, 42)

    @unittest.expectedFailure
    def test_invalid_kwargs_in_valid_kwargs(self):
        """Test invalid keyword in middle of
        valid keywords"""
        self.r1.update(y=2, cat=42, width=9)
        self.assertEqual(self.r1.cat, 42)

    def test_invalid_kwargs_in_valid_kwargs_pass(self):
        """Test invalid keyword in middle of
        valid keywords"""
        self.r1.update(y=2, cat=42, width=9)
        self.assertEqual(self.r1.y, 2)
        self.assertEqual(self.r1.width, 9)

    def test_valid_keyword_invalid_arg(self):
        """Update valid keyword with
        invalid type passed"""
        with self.assertRaises(TypeError):
            self.r1.update(y=[4, 5])


class TestToDictionary(unittest.TestCase):
    """Test to_dictionary method"""
    def setUp(self):
        """Instantiate new Square object and
        save it into dictionary for use. Reset
        number of objects to 0 before each test.
        """
        Base.reset_nb_objects()
        self.r1 = Rectangle(4, 3, 2, 9, 710)
        self.r1_dict = self.r1.to_dictionary()

    def tearDown(self):
        """Delete Square instance"""
        del self.r1

    def test_return_type(self):
        """Test that dictionary is returned"""
        self.assertEqual(type(self.r1_dict), dict)

    def test_to_dictionary(self):
        """Test correct dictionary return"""
        self.assertEqual(self.r1_dict, {'x': 2, 'y': 9, 'id': 710,
                                        'height': 3, 'width': 4})

    def test_update_to_dictionary(self):
        """Test correct dictionary return with updated args"""
        self.r1.update(id=42)
        r1_dict = self.r1.to_dictionary()
        self.assertEqual(r1_dict, {'x': 2, 'y': 9, 'id': 42,
                                   'height': 3, 'width': 4})

    def test_same_attrs_diff_obj(self):
        """Update rectangle with same attributes as
        other rectangle object, check they are
        different objects"""
        r2 = Rectangle(3, 4)
        r2.update(**self.r1_dict)
        self.assertIsNot(self.r1, r2)
