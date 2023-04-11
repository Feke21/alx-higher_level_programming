#!/usr/bin/python3
""" is_kind_of_class module """


def is_kind_of_class(obj, a_class):
    """ return true if obj is instance or inherited instance of class, else false """
    return isinstance(obj, a_class)
