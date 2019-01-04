#!/usr/bin/python3
class Square:
    """Square that is instantiated with size

    Attributes:
        __size (int, optional): instantizes a Square with a defined size
        __position (tuple of ints, optional): Position of the Square
    """
    __size = None
    __position = None

    def __init__(self, size=0, position=(0, 0)):
        """Instantation of Square class with optional size and position"""
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """Property getter of private attribute size

        Property setter: size(self, value) sets the size of the Square
        """
        return self.__size

    @size.setter
    def size(self, value):
        self.__size = value
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

    @property
    def position(self):
        """Property getter of private attribute position

        Property setter: position(self, value) sets position of Square
        """
        return self.__position

    @position.setter
    def position(self, value):
        self.__position = value
        if type(value) is not tuple or len(value) != 2:
            raise TypeError('position must be a tuple of 2 positive integers') 
        if not all(isinstance(n, int)) or not all(n > 0 for n in range(value)):
            raise TypeError('position must be a tuple of 2 positive integers')

    def area(self):
        """Returns the current square area"""
        return self.__size ** 2

    def my_print(self):
        """Prints a hashtag square using the size of the square"""
        if self.__size == 0:
            print('')
        for i in range(self.__position[1]):
            print('')
        for i in range(self.__size):
            print(' ' * self.__position[0], end='')
            print('#' * self.__size)
