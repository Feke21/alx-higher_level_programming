#!/usr/bin/python3
""" rectangle module """
from models.base import base


class Rectangle(Base):
    """ creates a class named rectangle inherited from base """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ initialization """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ return width """
        return self.__width

    @width.setter
    def width(self, width):
        """ get width """
        self.check('width', width)
        self.__width = width

    @property
    def height(self):
        """ return height """
        return self.__height

    @height.setter
    def height(self, height):
        """ get height """
        self.check('height', height)
        self.__height = height

    @property
    def x(self):
        """ return x """
        return self.__x

    @x.setter
    def x(self, x):
        """ get x """
        self.check('x', x, False)
        self.__x = x

    @property
    def y(self):
        """ return y """
        return self.__y

    @y.setter
    def y(self, y):
        """ get y """
        self.check('y', y, False)
        self.__y = y

    def area(self):
        """ return area """
        return self.__width * self.__height

    def display(self):
        """ print the rectangle """
        for y in range(self.y):
            print()
        for column in range(self.height):
            for x in range(self.x):
                print(' ', end='')
            for row in range(self.width):
                print("#", end='')
            print()

    def update(self, *args, **kwargs):
        """ assign argument to each attribute """
        tlist = (self.id, self.width, self.height, self.x, self.y)
        if args:
            self.id, self.width, self.height, self.x, self.y = \
                    args + tlist[len(args):len(tlist)]
        elif kwargs:
            for (key, value) in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """ return dict rep of rectangle """
        return {'x': self.x, 'y':self.y, 'id':self.id, 'height':self.height, 'width':self.width}

    def __str__(self):
        """ str method """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x, self.y, self.width, self.height)

    def check(self, key, value, less_eq=True):
        """ check for error """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(key))
        if less_eq:
            if value <= 0:
                raise ValueError("{} must be > 0".format(key))
        else:
            if value < 0:
                raise ValueError("{} must be >= 0".format(key))
