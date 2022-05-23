#!/usr/bin/env python3
"""489#4"""

import numpy as np
sensitivity = __import__('1-sensitivity').sensitivity
precision = __import__('2-precision').precision


def f1_score(confusion):
    """calculates the F1 score of a confusion matrix"""
    TPR = sensitivity(confusion)
    PPV = precision(confusion)
    return 2 * ((PPV * TPR) / (PPV + TPR))
