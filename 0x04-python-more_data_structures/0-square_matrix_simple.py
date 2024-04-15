#!/usr/bin/python3
"""DOC"""


def square_matrix_simple(matrix=[]):
<<<<<<< HEAD
    """DOC"""
   #mat = []
   #for i in matrix:
   #    row = []
   #    for x in i:
   #        row.append(x**2)
   #    mat.append(row)
   #return mat
    mat = matrix.apply(map(Lambda x**2: x))
    return mat
=======
    """DOCs"""
    mat = [list(map(lambda x: x ** 2, sublist)) for sublist in matrix]
    return mat
>>>>>>> dad0df2209a5241a5fbcd24222e298ec00d8fc5e
