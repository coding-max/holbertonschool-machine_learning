#!/usr/bin/env python3
"""475#16 - DeepNeuralNetwork"""

import numpy as np


class DeepNeuralNetwork:
    """ defines a deep neural network
    performing binary classification"""

    def __init__(self, nx, layers):
        """class constructor"""
        if not isinstance(nx, int):
            raise TypeError("nx must be an integer")
        if nx < 1:
            raise ValueError("nx must be a positive integer")
        if (not isinstance(layers, list) or len(layers) == 0 or
           any(not isinstance(layer, int) for layer in layers) or
           any(layer < 1 for layer in layers)):
            raise TypeError('layers must be a list of positive integers')
        self.L = len(layers)
        self.cache = self.weights = {}
        for i in range(self.L):
            w = 'W' + str(i + 1)
            b = 'b' + str(i + 1)
            prev = layers[i - 1] if i else nx
            sqrt = np.sqrt(2 / prev)
            self.weights[w] = np.random.randn(layers[i], prev) * sqrt
            self.weights[b] = np.zeros(shape=(layers[i], 1))
