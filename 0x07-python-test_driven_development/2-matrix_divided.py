#!/usr/bin/python3
"""
Matrix-divided module
Matrix and div as arguments
Returns a new matrix
"""


def matrix_divided(matrix, div):
    """ If statement """
    if type(matrix) != list:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    size = None
    for m in matrix:
        if type(m) != list:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        if size is None:
            size = len(m)
        elif size != len(m):
            raise TypeError("Each row of the matrix must have the same size")
        for n in m:
            if type(n) != int and type(n) != float:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            if type(div) != int and type(div) != float:
                raise TypeError("div must be a number")
            if div == 0:
                raise ZeroDivisionError("division by zero")
            return [[round(n / div, 2) for n in m] for m in matrix]
