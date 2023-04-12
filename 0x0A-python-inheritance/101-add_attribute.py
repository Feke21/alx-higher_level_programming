#!/usr/bin/python3
""" add_attribute module """


def add_attribute(an_obj, an_attr, a_value):
    """ function that adds a new attribute to an object if it’s possible """
    if not hasattr(an_obj, '__slots__') and not hasattr(an_obj, '__dict__'):
        raise TypeError("can't add new attribute")
    if hasattr(an_obj, '__slots__') and not hasattr(an_obj, an_attr):
        raise TypeError("can't add new attribute")

    setattr(an_obj, an_attr, a_value)
