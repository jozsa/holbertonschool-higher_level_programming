#!/usr/bin/python3
class BaseGeometry:
    """
    BaseGeometry class with non-implemented area() method
    """
    def area(self):
        """Unimplemented method"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Checks whether or not value is an integer more than 0"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
