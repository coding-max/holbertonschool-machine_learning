#!/usr/bin/env python3
"""487#0"""

import numpy as np
import statistics


def normalization_constants(X):
    """calculates the normalization (standardization) constants of a matrix"""
    mean = np.mean(X, axis=0)
    variance = np.mean((X-mean) ** 2, axis=0)

    return mean, variance
