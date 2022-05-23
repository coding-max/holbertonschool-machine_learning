#!/usr/bin/env python3
"""489#2"""

import numpy as np


def precision(confusion):
    """calculates the precision (PPV) for each class in a confusion matrix"""
    return np.diagonal(confusion) / np.sum(confusion, axis=0)
