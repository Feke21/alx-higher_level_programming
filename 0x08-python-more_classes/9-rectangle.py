#!/usr/bin/python3
""" Defines a rectangle class """


class Rectangle:
    """ Rectangle class attributes """
    number_of_instances = 0
    print_symbol = '#'

    """ __init__ func """
    def __init__(self, width=0, height=0):
        """ Initialize width and height """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
        """ Rectangle in hash char form """
        if self.__width == 0 or self.__height == 0:
            return ''
        res = ''
        for i in range(self.__height):
            for j in range(self.__width):
                res += str(self.print_symbol)
            res += '\n'
        return res[:-1]

    def __repr__(self):
        """ Repr func """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """ Del func """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ If statements """
        if type(rect_1) != Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) != Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        if rect_1.area() < rect_2.area():
            return rect_2

    @classmethod
    def square(cls, size=0):
        """ Returns a new Rectangle instance """
        return cls(size, size)
