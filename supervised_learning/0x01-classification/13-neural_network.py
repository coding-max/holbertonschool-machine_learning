#!/usr/bin/env python3
"""475#13 - NeuralNetwork Gradient Descent"""

import numpy as np


class NeuralNetwork:
    """defines a neural network with one hidden layer
    performing binary classification"""

    def __init__(self, nx, nodes):
        """class constructor"""
        if not isinstance(nx, int):
            raise TypeError("nx must be an integer")
        if nx < 1:
            raise ValueError("nx must be a positive integer")
        if not isinstance(nodes, int):
            raise TypeError('nodes must be an integer')
        if nodes < 1:
            raise ValueError('nodes must be a positive integer')
        self.__W1 = np.random.normal(size=(nodes, nx))
        self.__b1 = np.zeros([nodes, 1])
        self.__A1 = 0
        self.__W2 = np.random.normal(size=(1, nodes))
        self.__b2 = 0
        self.__A2 = 0

    @property
    def W1(self):
        """returns the weights vector for the hidden layer"""
        return self.__W1

    @property
    def b1(self):
        """returns the bias for the hidden layer"""
        return self.__b1

    @property
    def A1(self):
        """returns the activated output for the hidden layer"""
        return self.__A1

    @property
    def W2(self):
        """returns the weights vector for the output layer"""
        return self.__W2

    @property
    def b2(self):
        """returns the bias for the output layer"""
        return self.__b2

    @property
    def A2(self):
        """returns the weights vector for the output layer"""
        return self.__A2

    def forward_prop(self, X):
        """calculates the forward propagation of the neural network"""
        x = np.matmul(self.W1, X) + self.b1
        self.__A1 = 1 / (1 + np.exp(-x))
        x = np.matmul(self.W2, self.__A1) + self.b2
        self.__A2 = 1 / (1 + np.exp(-x))
        return self.A1, self.A2

    def cost(self, Y, A):
        """calculates the cost of the model using logistic regression"""
        costs = (Y * np.log(A)) + ((1 - Y) * np.log(1.0000001 - A))
        return np.sum(costs) * (-1 / A.shape[1])

    def evaluate(self, X, Y):
        """evaluates the neural network's predictions"""
        self.forward_prop(X)
        prediction = np.where(self.A2 >= 0.5, 1, 0)
        cost = self.cost(Y, self.A2)
        return prediction, cost

    def gradient_descent(self, X, Y, A1, A2, alpha=0.05):
        """calculates one pass of gradient descent on the neural network"""
        dz2 = A2 - Y
        dz1 = np.dot(self.__W2.T, dz2) * A1 * (1 - A1)
        dw1 = np.matmul(dz1, X.T) / A1.shape[1]
        dw2 = np.matmul(dz2, A1.T) / A2.shape[1]
        self.__W1 = self.W1 - (alpha * dw1)
        self.__b1 = self.b1 - (alpha * dz1.mean(axis=1, keepdims=True))
        self.__W2 = self.W2 - (alpha * dw2)
        self.__b2 = self.b2 - (alpha * dz2.mean(axis=1, keepdims=True))
