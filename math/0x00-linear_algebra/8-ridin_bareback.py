#!/usr/bin/env python3
"""467#8 - Ridin' Bareback"""


def mat_mul(mat1, mat2):
    """performs matrix multiplication"""
    matrix = []
    number_of_rows = len(mat1[0])
    number_of_columns = len(mat2)
    if (number_of_rows == number_of_columns):
        for i in range(len(mat1)):
            col = []
            for j in range(len(mat2[0])):
                element = 0
                for k in range(len(mat1[0])):
                    element += mat1[i][k] * mat2[k][j]
                col.append(element)    
            matrix.append(col)
        return matrix
    return None
