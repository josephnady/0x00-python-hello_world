#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    yy = list(map(lambda lst: list(map(lambda x: x*x, lst)),matrix))
    return  yy