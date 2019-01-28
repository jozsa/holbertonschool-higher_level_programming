#!/usr/bin/python3
"""
This module has one class, Square,
inherited from Rectangle
"""
from models.base import Base
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square instantiated with id/size/x/y

    Attributes:
        id (any, optional): id of new square
        size (int, required): size of new square
        x (int, optional): x-axis of new square
        y (int, optional): y-axis of new square
    """
    def __init__(self, size, x=0, y=0, id=None):
        """Instantation of Square class with:
        required size, optional x & y, and id
        inherited from Rectangle class which
        inherits from Base
        """
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        """Property getter of private attribute size

        Property setter: size(self, value) sets the size
        of the new square instance
        """
        return self.__size

    @size.setter
    def size(self, value):
        self.__size = value
        self.width = value
        self.height = value

    def __str__(self):
        """Overrides __str__ builtin so it will return
        a string representation of the Square"""
        return '[Square] ({}) {}/{} - {}' \
            .format(self.id, self.x, self.y, self.width)

    def update(self, *args, **kwargs):
        """Updates attributes of Square objects:
        Argument 1: id
        Argument 2: size
        Argument 3: x
        Argument 4: y

        If kwargs is passed,the order does not matter
        """
        attrs = ['id', 'size', 'x', 'y']
        arg_list = zip(attrs, args) if args else kwargs.items()
        for k, v in arg_list:
            if k in attrs:
                setattr(self, k, v)

    def to_dictionary(self):
        """Returns the dictionary representation of
        a square object."""
        new_dict = {k.replace('_Square__', '').replace('_Rectangle__', ''): v
                    for k, v in self.__dict__.items()}
        del_keys = ['width', 'height']
        for i in del_keys:
            del new_dict[i]
        return new_dict
