#!/usr/bin/python3
"""DOC"""


def square_matrix_simple(matrix=[]):
    """DOCs"""
    mat = [list(map(lambda x: x ** 2, sublist)) for sublist in matrix]
    return mat
