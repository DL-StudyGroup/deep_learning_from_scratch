# coding: utf-8
import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def relu(x):
    return np.maximum(0, x)


x = np.array([1.0, 0.5])

w1 = np.array([[0.1, 0.3, 0.5], [0.2, 0.4, 0.6]])
b1 = np.array([0.1, 0.2, 0.3])
a1 = sigmoid(np.dot(x, w1) + b1)

w2 = np.array([[0.1, 0.4], [0.2, 0.5], [0.3, 0.6]])
b2 = np.array([0.1, 0.2])
a2 = relu(np.dot(a1, w2) + b2)

w3 = np.array([[0.1, 0.3], [0.2, 0.4]])
b3 = np.array([0.1, 0.2])
a3 = np.dot(a2, w3) + b3

print(a2)