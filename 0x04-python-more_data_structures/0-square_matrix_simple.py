#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    powmatrix = [[number**2 for number in rows] for rows in matrix]
    return powmatrix
