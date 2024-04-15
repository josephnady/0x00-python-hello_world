#!/usr/bin/python3
"""DOC"""


def square_matrix_simple(matrix=[]):
    """DOC"""
    mat = []
    for i in matrix:
        row = []
        for x in i:
            row.append(x**2)
        mat.append(row)
    return mat
