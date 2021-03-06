#!/usr/bin/python3
class Square:
    """Square that is instantiated with size

    Attributes:
        __size (int): instantizes a Square with a defined size
    """
    __size = None

    def __init__(self, size=0):
        """Instantation of Square class with optional size"""
        self.__size = size

    @property
    def size(self):
        """Getter property of private attribute size

        size(self, value) sets the size of the Square
        """
        return self.__size

    @size.setter
    def size(self, value):
        self.__size = value
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """Returns the current square area"""
        return self.__size ** 2

    def __lt__(self, other):
        return self.area() < other.area()

    def __le__(self, other):
        return self.area() <= other.area()

    def __eq__(self, other):
        return self.area() == other.area()

    def __ne__(self, other):
        return self.area() != other.area()

    def __gt__(self, other):
        return self.area() > other.area()

    def __ge__(self, other):
        return self.area() >= other.area()
