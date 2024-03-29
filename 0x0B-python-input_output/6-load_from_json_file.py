#!/usr/bin/python3
""" load_from_json_file module """
import json


def load_from_json_file(filename):
    """ loads an object from JSON file """
    with open(filename, "r") as f:
        my_obj = json.load(f)
        return my_obj
