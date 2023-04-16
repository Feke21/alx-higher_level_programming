#!/usr/bin/python3
""" 11-student module """


class Student:
    """ creates a class named Student """
    def __init__(self, first_name, last_name, age):
        """ initializes the names and age """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ retrieves dict rep of Student """
        if type(attrs) is list and all([type(i) == str for i in attrs]):
            return {j: k for j, k in self.__dict__.items() if j in attrs}
        else:
            return self.__dict__.copy()

    def reload_from_json(self, json):
        """ loads attributes from json """
        for key, value in json.items():
            self.__dict__[key] = value
