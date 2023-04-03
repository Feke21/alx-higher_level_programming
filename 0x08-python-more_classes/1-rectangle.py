#!/usr/bin/python3
""" Defines a Rectangle class """


class Rectangle:
    """ Defines a func called __init__ """
    def __init__(self, width=0, height=0):
        """ Initializes the width and height with self """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ Returns __width of self """
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
        """ Returns __height of self """
        return self.__height

    @height.setter
    def height(self, value):
        """ If statement """
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
