#!/usr/bin/python3
"""Defines a class named Square"""


class Square:
    """Defines a fumtion named __init__"""
    def __init__(self, size=0):
        """If statement"""
        if type(size) != int:
            """Raise an error"""
            raise TypeError("size must be an integer")
        elif size < 0:
            """Raise an error"""
            raise ValueError("size must be >= 0")
        else:
            """Initializes __size of self with size"""
            self.__size = size
    """Defines area function or public instance method"""
    def area(self):
        """Returns area"""
        return self.__size ** 2
