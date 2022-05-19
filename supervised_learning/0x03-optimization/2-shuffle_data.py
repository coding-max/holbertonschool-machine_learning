#!/usr/bin/env python3
"""487#2"""

import numpy as np


def shuffle_data(X, Y):
    """shuffles the data points in two matrices the same way"""
    permutation = np.random.permutation(X.shape[0])
    return X[permutation, :], Y[permutation, :]
