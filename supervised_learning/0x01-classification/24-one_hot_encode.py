#!/usr/bin/env python3
"""475#24 - One-Hot Encode"""

import numpy as np


def one_hot_encode(Y, classes):
    """converts a numeric label vector into a one-hot matrix"""
    if not isinstance(Y, np.ndarray):
        return None
    matrix = np.eye(classes)[Y].T
    return matrix if not None else None
