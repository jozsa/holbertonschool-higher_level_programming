#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square subclass of Rectangle instantiated with size

    Attributes:
        size (int, required): size to instantiate square with
    """
    def __init__(self, size):
        """Instantation of Square class instance with
        required size. Instantation is inherited from
        Rectangle class with the addition of size"""
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
