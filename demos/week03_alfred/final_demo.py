import numpy as np


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def relu(x):
    return np.maximum(0.0, x)


X = np.array([1.0, 0.5])
W1 = np.array([[0.1, 0.3, 0.5], [0.2, 0.4, 0.6]])
B1 = np.array([0.1, 0.2, 0.3])
W2 = np.array([[0.1, 0.4], [0.2, 0.5], [0.3, 0.6]])
B2 = np.array([0.1, 0.2])
W3 = np.array([[0.1, 0.3], [0.2, 0.4]])
B3 = np.array([0.1, 0.2])

a1 = np.dot(X, W1) + B1
z1 = sigmoid(a1)

a2 = np.dot(z1, W2) + B2
z2 = relu(a2)

y = z2 + B3
print("X:", X)
print("------------")
print("a1:", a1)
print("z1:", z1)
print("a2:", a2)
print("z2:", z2)
print("-------------")
print("the final y: ", y)
