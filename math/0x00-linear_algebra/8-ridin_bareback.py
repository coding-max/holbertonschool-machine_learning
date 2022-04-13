#!/usr/bin/env python3
"""467#8 - Ridin' Bareback"""


def mat_mul(mat1, mat2):
    """performs matrix multiplication"""
    rowsInMat1 = len(mat1)
    columnsInMat1 = len(mat1[0])
    rowsInMat2 = len(mat2)
    columnsInMat2 = len(mat2[0])
    if (columnsInMat1 == rowsInMat2):
        matrixProduct = []
        for i in range(rowsInMat1):
            row = []
            for j in range(columnsInMat2):
                element = 0
                for k in range(columnsInMat1):
                    element += mat1[i][k] * mat2[k][j]
                row.append(element)
            matrixProduct.append(row)
        return matrixProduct
    return None
