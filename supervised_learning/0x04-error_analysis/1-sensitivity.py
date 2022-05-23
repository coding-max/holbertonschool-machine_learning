#!/usr/bin/env python3
"""489#1"""

import numpy as np


def sensitivity(confusion):
    """calculates the sensitivity for each class in a confusion matrix"""
    return np.diagonal(confusion) / np.sum(confusion, axis=1)
