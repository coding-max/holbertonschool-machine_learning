#!/usr/bin/env python3
"""475#5 - Neuron Gradient Descent"""

import numpy as np


class Neuron:
    """defines a single neuron performing binary classification"""

    def __init__(self, nx):
        """class constructor"""
        if not isinstance(nx, int):
            raise TypeError("nx must be an integer")
        if nx < 1:
            raise ValueError("nx must be a positive integer")
        self.__W = np.random.normal(size=(1, nx))
        self.__b = 0
        self.__A = 0

    @property
    def W(self):
        """resturns the weights vector for the neuron"""
        return self.__W

    @property
    def b(self):
        """returns the bias for the neuron"""
        return self.__b

    @property
    def A(self):
        """returns the activated output of the neuron"""
        return self.__A

    def forward_prop(self, X):
        """calculates the forward propagation of the neuron"""
        x = np.matmul(self.W, X) + self.b
        self.__A = 1 / (1 + np.exp(-x))
        return self.A

    def cost(self, Y, A):
        """calculates the cost of the model using logistic regression"""
        costs = (Y * np.log(A)) + ((1 - Y) * np.log(1.0000001 - A))
        return np.sum(costs) * (-1 / A.shape[1])

    def evaluate(self, X, Y):
        """evaluates the neuron's predictions"""
        self.forward_prop(X)
        prediction = np.where(self.A >= 0.5, 1, 0)
        cost = self.cost(Y, self.A)
        return prediction, cost

    def gradient_descent(self, X, Y, A, alpha=0.05):
        """calculates one pass of gradient descent on the neuron"""
        dz = A - Y
        dw = np.matmul(X, dz.T) / A.shape[1]
        db = np.sum(dz) / A.shape[1]
        self.__W = self.W - alpha * dw.T
        self.__b = self.b - alpha * db
