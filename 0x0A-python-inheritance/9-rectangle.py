#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle instantiated with width and height

    Attributes:
        width (int, required): width to instantiate rectangle with
        height (int, required): height to instantiate rectangle with
    """
    def __init__(self, width, height):
        """Instantation of Rectangle class with
        required width and height. Width and height
        must be integers."""
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        return self.__height * self.__width

    def __str__(self):
        return '[Rectangle] {}/{}'.format(self.__width, self.__height)
