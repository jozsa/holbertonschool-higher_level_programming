#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    size = len(matrix[0])
    for row in range(len(matrix)):
        for column in range(size):
            if column < size - 1:
                sep = ' '
            else:
                sep = ''
            print('{:d}'.format(matrix[row][column]), end=sep)
        print()
