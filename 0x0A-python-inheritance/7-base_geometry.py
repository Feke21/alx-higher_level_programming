#!/usr/bin/python3
""" 7-base_geometry module """


class BaseGeometry:
    """ defines base geometry class """
    def area(self):
        """ raise an excption with a message """
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """ if statement """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
