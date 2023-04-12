#!/usr/bin/python3
""" 8-rectangle module """
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ recatngle class that inherits from base geometry """
    def __init__(self, width height):
        """ initializes the width and height """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
