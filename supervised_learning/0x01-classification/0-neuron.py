#!/usr/bin/env python3
"""475#0 - Neuron"""

import numpy as np


class Neuron:
    """defines a single neuron performing binary classification"""

    def __init__(self, nx):
        """class constructor"""
        if not isinstance(nx, int):
            raise TypeError("nx must be a integer")
        if nx < 1:
            raise ValueError("nx must be positive")
        self.W = np.random.normal(size=nx)
        self.b = 0
        self.A = 0
