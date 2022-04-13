#!/usr/bin/env python3
"""467#3 - Flip Me Over"""


def matrix_transpose(matrix):
    """returns the transpose of a 2D matrix"""
    row = len(matrix[0])
    col = len(matrix)
    return [[matrix[i][j] for i in range(col)] for j in range(row)]
