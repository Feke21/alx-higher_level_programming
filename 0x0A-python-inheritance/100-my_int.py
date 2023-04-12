#!/usr/bin/python3
""" my_int module """


class MyInt(int):
    """
    MyInt inherits from class int
    but the behaviour of != and == is reversed
    """
    def __eq__(self, other):
        """ Equality is inequality """
        return super().__ne__(other)

    def __ne__(self, other):
        """ Inequality is equality """
        return super().__eq__(other)
