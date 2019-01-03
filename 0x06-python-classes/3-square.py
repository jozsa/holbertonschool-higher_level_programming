#!/usr/bin/python3
class Square:
    """Square that is instantiated with size

    Attributes:
        __size (int): instantizes a Square with a defined size
    """
    __size = None

    def __init__(self, size=0):
        """Instantation of Square class with size"""
        self.__size = size
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """Returns the current square area"""
        return self.__size ** 2
