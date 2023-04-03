#!/usr/bin/python3
""" Defines a rectangle class """


class Rectangle:
    """ Defines a func called __init__ """
    def __init__(self, width=0, height=0):
        """ Initializes width and height with self """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ Gets width """
        return self.__width

    @width.setter
    def width(self, value):
        """ If statement """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ Gets height """
        return self.__height

    @height.setter
    def height(self, value):
        """ If statement """
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ Returns area """
        return self.__width * self.__height

    def perimeter(self):
        """ Returns perimeter """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """ Returns rectangle i hash char form """
        if self.__width == 0 or self.__height == 0:
            return ''
        res = ''
        for i in range(self.__height):
            for j in range(self.__width):
                res += '#'
            res += '\n'
        return res[:-1]

    def __repr__(self):
        """ Repr func """
        return "Rectangle({}, {})".format(self.__width, self.__height)
