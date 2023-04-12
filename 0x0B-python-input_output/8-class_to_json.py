#!/usr/bin/python3
""" class_to_json module """


def class_to_json(obj):
    """
    returns dict rep with simple data structure
    """
    return obj.__dict__
