#!/usr/bin/python3
class BaseGeometry:
    """
    BaseGeometry class with non-implemented area() method
    """
    def area(self):
        """Unimplemented method"""
        raise Exception("area() is not implemented")
