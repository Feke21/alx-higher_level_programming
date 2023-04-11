#!/usr/bin/python3
"""
lookup - returns the list of available attributes and methods of an object
@obj: object
Return: list object
"""


def lookup(obj):
    """ return list of object """
    return dir(obj)
