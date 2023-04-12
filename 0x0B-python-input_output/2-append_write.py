#!/usr/bin/python3
""" append_write module """


def append_write(filename="", text=""):
    """
    appends a string at the end of a text
    and returns the nu, of char added
    """
    with open(filename, mode="a", encoding="UTF-8") as f:
        return (f.write(text))
