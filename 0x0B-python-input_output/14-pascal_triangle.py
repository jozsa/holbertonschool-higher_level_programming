#!/usr/bin/python3
"""pascal_triangle(n)

Returns a list of lists of integers
representing Pascal's triangle of n
"""


def pascal_triangle(n):
    """
    Returns a Pascal triangle of n
    """
    if n <= 0:
        return []
    if n == 1:
        return[[1]]
    pascal_tri = [[1], [1, 1]]
    for i in range(2, n):
        list_to_add = [x for x in range(i + 1)]
        for y in range(1, i):
            list_to_add[0] = 1
            list_to_add[i] = 1
            list_to_add[y] = pascal_tri[i - 1][y] + pascal_tri[i - 1][y - 1]
        pascal_tri.append(list_to_add)
    return pascal_tri
