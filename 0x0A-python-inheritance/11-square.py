#!/usr/bin/python3
""" 11-square module """
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Square class that inherits from Rectangle class """
    def __init__(self, size):
        """ initializes a square """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """ returns area """
        return self.__size ** 2

    def __str__(self):
        """ returns a square description """
        return str("[Square] {}/{}".format(self.__size, self.__size))
