#!/usr/bin/python3
"""lazy_matrix_mul(m_a, m_b)

One function that multiplies two matrices using NumPy
"""


import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Returns a new matrix with the multiplied values
    """
    return np.dot(m_a, m_b)
