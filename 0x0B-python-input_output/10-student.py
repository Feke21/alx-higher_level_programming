#!/usr/bin/python3
""" 10-student module """


class Student:
    """
    creates a class named Student with names and age
    based on 9-student.py
    """
    def __init__(self, first_name, last_name, age):
        """ initializes names and age """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ retrieves a dict rep of Student """
        if attrs != None:
            res = {i: self.__dict__[i] for i in self.__dict__.keys() & attrs}
            return res
        else:
            return self.__dict__
