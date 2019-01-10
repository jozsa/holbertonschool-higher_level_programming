#!/usr/bin/python3
"""lazy_matrix_mul(m_a, m_b)

One function that multiplies two matrices using NumPy
"""


import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Returns a new matrix with the multiplied values
    """

    if not isinstance(m_a, list):
        raise TypeError('m_a must be a list')
    if not isinstance(m_b, list):
        raise TypeError('m_b must be a list')
    if not all(isinstance(n, list) for n in m_a):
        raise TypeError('m_a must be a list of lists')
    if not all(isinstance(n, list) for n in m_b):
        raise TypeError('m_b must be a list of lists')
    if len(m_a) == 0 or len(m_a[0]) == 0:
        raise ValueError('m_a can\'t be empty')
    if len(m_b) == 0 or len(m_b[0]) == 0:
        raise ValueError('m_b can\'t be empty')
    for rows in m_a:
        if not all(isinstance(cols, (float, int)) for cols in rows):
            raise TypeError('m_a should contain only integers or floats')
    for rows in m_b:
        if not all(isinstance(cols, (float, int)) for cols in rows):
            raise TypeError('m_b should contain only integers or floats')
    if not all(len(rows) == len(m_a[0]) for rows in m_a):
        raise TypeError('each row of m_a must should be of the same size')
    if not all(len(rows) == len(m_b[0]) for rows in m_b):
        raise TypeError('each row of m_b must should be of the same size')
    if len(m_a[0]) != len(m_b):
        raise ValueError('m_a and m_b can\'t be multiplied')
    return np.dot(m_a, m_b)
