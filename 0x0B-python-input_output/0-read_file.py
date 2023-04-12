#!/usr/bin/python3
""" read_file module """


def read_file(filename=""):
    """ read a text file and print to stdout """
    with open(filename, "r", encoding="UTF-8") as i:
        for line in i:
            print(line, end="")
