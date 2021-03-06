#!/usr/bin/env python3
""" Python program to implement a deep neural network """
import numpy as np
import matplotlib.pyplot as plt


class DeepNeuralNetwork():
    """
        class DeepNeuralNetwork that defines a deep neural network
        performing binary classification.
        nx : is the number of input features
        layers : is a list representing the number of nodes
        in each layer of the network
        L: The number of layers in the neural network.
        cache: A dictionary to hold all intermediary values of the network.
        weights: A dictionary to hold all weights and biased of the network.

    """

    def __init__(self, nx, layers):
        """Class constructor"""

        if not isinstance(nx, int):
            raise TypeError('nx must be an integer')

        if nx < 1:
            raise ValueError('nx must be a positive integer')

        if not isinstance(layers, list) or len(layers) == 0:
            raise TypeError("layers must be a list of positive integers")

        self.__L = len(layers)
        self.__cache = {}
        self.__weights = {}

        for lay in range(self.L):
            if not isinstance(layers[lay], int) or layers[lay] <= 0:
                raise TypeError("layers must be a list of positive integers")
            if lay == 0:
                He = (np.random.randn(layers[lay], nx)
                      * np.sqrt(2 / nx))
                self.__weights["W{}".format(lay + 1)] = He
            else:
                He = (np.random.randn(layers[lay], layers[lay - 1])
                      * np.sqrt(2 / layers[lay - 1]))
                self.__weights["W{}".format(lay + 1)] = He
            self.__weights["b{}".format(lay + 1)] = np.zeros((layers[lay], 1))

    @property
    def L(self):
        return self.__L

    @property
    def cache(self):
        return self.__cache

    @property
    def weights(self):
        return self.__weights

    def forward_prop(self, X):
        """
            Add the public method def forward_prop with
            He et al. Matrix Mult. of Weights
            and X values (input data).
        """
        self.cache.update({'A0': X})
        for i in range(self.L):
            A = self.cache.get('A' + str(i))
            biases = self.weights.get('b' + str(i + 1))
            weights = self.weights.get('W' + str(i + 1))
            Z = np.matmul(weights, A) + biases
            self.cache.update({'A' + str(i + 1): 1 / (1 + np.exp(-Z))})

        return self.cache.get('A' + str(i + 1)), self.cache

    def cost(self, Y, A):
        """
            Method to calculate the cost of the model
            using logistic regression
            Y : contains the correct labels for the input data.
            A : contains the activated output of the neuron for each.
        """

        cost = - (1 / Y.shape[1]) * np.sum(np.multiply(Y, np.log(A)) +
                                           np.multiply(1 - Y,
                                                       np.log(1.0000001 - A)))
        return cost

    def evaluate(self, X, Y):
        """
            Method to Evaluates the neuron’s predictions.
            X : is a numpy.ndarray with shape (nx, m)
                that contains the input data.
            Y : is a numpy.ndarray with shape (1, m)
                that contains the correct labels for the input data.
        """

        A, _ = self.forward_prop(X)
        NeuronEvaluation = np.where(
            A <= 0.5, 0, 1), self.cost(
            Y, A)

        return NeuronEvaluation

    def gradient_descent(self, Y, cache, alpha=0.05):
        """
            Y is a numpy.ndarray with shape (1, m) that contains
            the correct labels for the input data
            cache is a dictionary containing all the intermediary
            values of the network
            alpha is the learning rate
            Updates the private attribute __weights
        """

        NumberOfLayers = range(self.L, 0, -1)
        NumberOfElements = Y.shape[1]
        DifferenceStorage = 0
        weights = self.weights.copy()

        for i in NumberOfLayers:

            A = cache.get('A' + str(i))
            A_prev = cache.get('A' + str(i - 1))
            weights_i = weights.get('W' + str(i))
            weights_n = weights.get('W' + str(i + 1))
            biases = weights.get('b' + str(i))

            if i == self.L:
                Difference = A - Y
            else:
                Difference = np.matmul(
                    weights_n.T, DifferenceStorage) * (A * (1 - A))

            GradientW = np.matmul(Difference, A_prev.T) / NumberOfElements
            biasAverage = np.sum(
                Difference, axis=1, keepdims=True) / NumberOfElements
            self.__weights['W' + str(i)] = weights_i - (GradientW * alpha)
            self.__weights['b' + str(i)] = biases - (biasAverage * alpha)
            DifferenceStorage = Difference

    def train(
            self,
            X,
            Y,
            iterations=5000,
            alpha=0.05,
            verbose=True,
            graph=True,
            step=100):
        """
            Trains the neuron
            X is a numpy.ndarray with shape (nx, m) that contains
            the input data
                nx is the number of input features to the neuron
                m is the number of examples
            Y is a numpy.ndarray with shape (1, m) that contains
            the correct labels for the input data
            iterations is the number of iterations to train over
                if iterations is not an integer, raise a TypeError with the
                exception iterations must be an integer
                if iterations is not positive, raise a ValueError with the
                exception iterations must be a positive integer
            alpha is the learning rate
                if alpha is not a float, raise a TypeError with the
                exception alpha must be a float
                if alpha is not positive, raise a ValueError with the
                exception alpha must be positive
            All exceptions should be raised in the order listed above
            Updates the private attributes __W, __b, and __A
            You are allowed to use one loop
            Returns the evaluation of the training data after iterations
            of training have occurred
        """

        if not isinstance(iterations, int):
            raise TypeError('iterations must be an integer')
        if iterations < 0:
            raise ValueError('iterations must be a positive integer')
        if not isinstance(alpha, float):
            raise TypeError('alpha must be a float')
        if alpha < 0:
            raise ValueError('alpha must be positive')

        Costs = list()
        IterationsStorage = [*list(range(iterations)), iterations]

        for i in IterationsStorage:
            A, cost = self.evaluate(X, Y)

            if verbose and i % step == 0:
                print('Cost after ' + str(i) + ' iterations: ' + str(cost))
            Costs.append(cost)
            self.gradient_descent(Y, self.cache, alpha)

        if graph:
            plt.plot(IterationsStorage, Costs)
            plt.xlabel('iterations')
            plt.ylabel('cost')
            plt.title('Training cost')
            plt.show()

        return A, cost
