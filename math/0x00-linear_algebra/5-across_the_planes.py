#!/usr/bin/env python3
"""467#5 - Across The Planes"""


def add_matrices2D(mat1, mat2):
    """adds two matrices element-wise"""
    if len(mat1) != len(mat2) or len(mat1[0]) != len(mat2[0]):
        return None
    col = len(mat1[0])
    row = len(mat1)
    return [[(mat1[i][j] + mat2[i][j]) for j in range(row)] for i in range(col)]
