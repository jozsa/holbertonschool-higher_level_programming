#!/usr/bin/python3
class Square:
    """Square that is instantiated with size

    Attributes:
        size (no type): private attribute that instantizes Square
    """
    __size = None

    def __init__(self, __size):
        """Instantation of Square class with size"""
        self.__size = __size
