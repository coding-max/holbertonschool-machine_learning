#!/usr/bin/env python3
"""487#0"""

import numpy as np


def normalization_constants(X):
    """calculates the normalization (standardization) constants of a matrix"""
    return np.mean(X, axis=0), np.std(X, axis=0)
