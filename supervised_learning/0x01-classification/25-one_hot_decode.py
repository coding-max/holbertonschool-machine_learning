#!/usr/bin/env python3
"""475#25 - One-Hot Decode"""

import numpy as np


def one_hot_decode(one_hot):
    """converts a one-hot matrix into a vector of labels"""
    if isinstance(one_hot, np.ndarray) and len(one_hot.shape) == 2:
        return np.argmax(one_hot.T, axis=1)
    return None
