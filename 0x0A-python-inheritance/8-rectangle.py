#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle subclass of BaseGeometry instantiated with width and height

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
