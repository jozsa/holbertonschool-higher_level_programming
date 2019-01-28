#!/usr/bin/python3
from models.base import Base


class Rectangle(Base):
    """Rectangle instantiated with id/width/height/x/y

    Attributes:
        width (int, required): width of new instance
        height (int, required): height of new instance
        x (int, optional): x-axis of new instance
        y (int, optional): y-axis of new instance
        id (any, optional): id of new instance
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """Instantation of Rectangle class with:
        required width & height, optional x & y,
        and id inherited from Base class"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def integer_validator(self, name, value):
        """Checks the values passed into Rectangle
        instantation for validity"""
        if type(value) is not int:
            raise TypeError('{} must be an integer'.format(name))
        if (name is 'x' or name is 'y') and value < 0:
            raise ValueError('{} must be >= 0'.format(name))
        if (name is 'width' or name is 'height') and value <= 0:
            raise ValueError('{} must be > 0'.format(name))

    @property
    def width(self):
        """Property getter of private attribute width

        Property setter: width(self, value) sets the width
        of the new Rectangle instance
        """
        return self.__width

    @width.setter
    def width(self, value):
        self.integer_validator('width', value)
        self.__width = value

    @property
    def height(self):
        """Property getter of private attribute height

        Property setter: height(self, value) sets the height
        of the new Rectangle instance
        """
        return self.__height

    @height.setter
    def height(self, value):
        self.integer_validator('height', value)
        self.__height = value

    @property
    def x(self):
        """Property getter of private attribute x

        Property setter: x(self, value) sets the x axis
        of the new Rectangle instance
        """
        return self.__x

    @x.setter
    def x(self, value):
        self.integer_validator('x', value)
        self.__x = value

    @property
    def y(self):
        """Property getter of private attribute x

        Property setter: y(self, value) sets the y axis
        of the new Rectangle instance
        """
        return self.__y

    @y.setter
    def y(self, value):
        self.integer_validator('y', value)
        self.__y = value

    def area(self):
        """Returns the area of the current rectangle"""
        return self.width * self.height

    def display(self):
        """Prints the current rectangle
        # - using width/height
        Offset (newline/space) using x/y"""
        print('\n' * self.y, end='')
        for rows in range(self.height):
            print((' ' * self.x) + ('#' * self.width))

    def __str__(self):
        """Overrides __str__ builtin so it will return
        a string representation of the Rectangle"""
        return '[Rectangle] ({}) {}/{} - {}/{}' \
            .format(self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """Updates attributes of Rectangle objects:
        Argument 1: id
        Argument 2: width
        Argument 3: height
        Argument 4: x
        Argument 5: y

        If kwargs is passed, the order does not matter.
        """
        attrs = ['id', 'width', 'height', 'x', 'y']
        arg_list = zip(attrs, args) if args else kwargs.items()
        for k, v in arg_list:
            if k in attrs:
                setattr(self, k, v)

    def to_dictionary(self):
        """Returns the dictionary representation of
        a rectangle object."""
        return {k.replace('_Rectangle__', ''): v
                for k, v in self.__dict__.items()}
