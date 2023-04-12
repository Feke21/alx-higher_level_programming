#!/usr/bin/python3
""" 9-rectangle module """
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ rectangle class that inherits from base geometry """
    def __init__(self, width, height):
        """ initializes the width and height """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """ returns area """
        return self.__width * self.__height

    def __str__(self):
        """ returns rectangle description """
        return str("[Rectangle] {}/{}".format(self.__width, self.__height))
