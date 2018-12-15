import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def relu(x):
    return np.maximum(0.0, x)

x = [[1.0, 0.5]]
b1 = [[0.1, 0.2, 0.3]]
w1 = [[0.1, 0.3, 0.5], [0.2, 0.4, 0.6]]

w2 = [[0.1, 0.4], [0.2, 0.5], [0.3, 0.6]]
b2 = [[0.1, 0.2]]

w3 = [[0.1, 0.3], [0.2, 0.4]]
b3 = [[0.1, 0.2]]

x = np.float32(x)
w1 = np.float32(w1)

a1 = np.dot(x, w1) + b1
z1 = sigmoid(a1)

print(a1)
print(a1.shape)
print(z1)
print(z1.shape)

a2 = np.dot(z1, w2) + b2
z2 = relu(a2)

print(z2)
print(z2.shape)

a3 = np.dot(z2, w3) + b3

print(a3)
print(a3.shape)


