#!/usr/bin/python3
""" rectangle module """
from models.base import Base


class Rectangle(Base):
    """ create a class named rectangle that inherits from base """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ initilaization """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ returns width """
        return self.__width

    @width.setter
    def width(self, width):
        """ sets width """
        self.__width = width

    @property
    def height(self):
        """ returns height """
        return self.__height

    @height.setter
    def height(self, height):
        """ sets height """
        self.__height = height

    @property
    def x(self):
        """ returns x """
        return self.__x

    @x.setter
    def x(self, x):
        """ sets x """
        self.__x = x

    @property
    def y(self):
        """ returns y """
        return self.__y

    @y.setter
    def y(self, y):
        """ sets y """
        self.__y = y
