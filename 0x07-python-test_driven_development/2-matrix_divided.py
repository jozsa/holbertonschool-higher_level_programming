#!/usr/bin/python3
"""matrix_divided(matrix, div)

This module divides each element of a given matrix by a given divisor
"""


def matrix_divided(matrix, div):
    """
    Returns a new matrix with all the divided elements
    """
    if not isinstance(div, (float, int)):
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')
    if not isinstance(matrix, list):
        raise TypeError('matrix must be a matrix '
                        '(list of lists) of integers/floats')
    if not all(isinstance(rows, list) for rows in matrix):
        raise TypeError('matrix must be a matrix '
                        '(list of lists) of integers/floats')
    if not all(len(rows) == len(matrix[0]) for rows in matrix):
        raise TypeError('Each row of the matrix must have the same size')
    for rows in matrix:
        if not all(isinstance(cols, (float, int)) for cols in rows):
            raise TypeError('matrix must be a matrix '
                            '(list of lists) of integers/floats')
    newmatrix = [[round(cols/div, 2) for cols in rows] for rows in matrix]
    return newmatrix
