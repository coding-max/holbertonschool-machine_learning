#!/usr/bin/env python3
"""467#7 - Gettin' Cozy"""


def cat_matrices2D(mat1, mat2, axis=0):
    """concatenates two matrices along a specific axis"""
    same_columns = len(mat1[0]) == len(mat2[0])
    same_rows = len(mat1) == len(mat2)
    if ((axis == 0 and same_rows) or (axis == 1 and same_columns)):
        return None
    matrix = None
    if (axis == 0):
        mat1_cpy = [element.copy() for element in mat1]
        mat2_cpy = [element.copy() for element in mat2]
        matrix = mat1_cpy + mat2_cpy
    else:
        matrix = [mat1[i] + mat2[i] for i in range(len(mat1))]
    return matrix
