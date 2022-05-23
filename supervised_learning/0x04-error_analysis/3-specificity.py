#!/usr/bin/env python3
"""489#3"""

import numpy as np


def specificity(confusion):
    """calculates the specificity (TNR) for each class in a confusion matrix"""
    FP = confusion.sum(axis=0) - np.diag(confusion)
    FN = confusion.sum(axis=1) - np.diag(confusion)
    TP = np.diag(confusion)
    TN = confusion.sum() - (FP + FN + TP)
    return TN / (TN + FP)
