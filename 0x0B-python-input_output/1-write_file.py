#!/usr/bin/python3
""" write_file module """


def write_file(filename="", text=""):
    """ writes a string to a text file and returns the num of characters written """
    with open(filename, mode="w", encoding="UTF-8") as f:
        return (f.write(text))
