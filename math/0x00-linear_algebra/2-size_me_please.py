#!/usr/bin/env python3
"""467#2 - Size Me Please"""


def matrix_shape(matrix):
    """calculates the shape of a matrix"""
    shape = [len(matrix)]
    while isinstance(matrix[0], list):
        shape.append(len(matrix[0]))
        matrix = matrix[0]
    return shape
