#!/usr/bin/python3
class Rectangle:
    """Rectangle instantiated with width and height

    Attributes:
        width (int, optional): width to instantiate rectangle with
        height (int, optional): height to instantiate rectangle with
    """
    def __init__(self, width=0, height=0):
        """Instantation of Rectangle class with
        optional height and width"""
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        """Property getter of private attribute width

        Property setter: width(self, value) sets the size of the Rectangle
        """
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        """Property getter of private attribute height

        Property setter: height(self, value) sets the size of the Rectangle
        """
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """Returns the current rectangle area"""
        return self.width * self.height

    def perimeter(self):
        """Returns the current rectangle perimeter"""
        if self.width == 0 or self.height == 0:
            perimeter = 0
        else:
            perimeter = (self.width * 2) + (self.height * 2)
        return perimeter
