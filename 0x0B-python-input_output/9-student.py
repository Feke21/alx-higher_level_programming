#!/usr/bin/python3
""" student module """


class Student:
    """
    creating a class called student
    """
    def __init__(self, first_name, last_name, age):
        """ initializes names and age """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ retrieves a dict rep of Student """
        return self.__dict__
