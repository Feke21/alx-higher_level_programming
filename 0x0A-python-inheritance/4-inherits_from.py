#!/usr/bin/python3
""" inherits_from module """


def inherits_from(obj, a_class):
    """ return if obj is an instance of a class that inherited 
    (directly or indirectly) from the specified class, else False
    """
    return isinstance(obj, a_class) and type(obj) != a_class
