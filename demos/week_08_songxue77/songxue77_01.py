import numpy as np


X = np.random.rand(2)
W = np.random.rand(2,3)
B = np.random.rand(3)

Y = np.dot(X,W) + B


A = np.array([1,2])
C = np.array([[1],[2]])

print(X.shape)
print(W.shape)
print(B.shape)
print(Y.shape)
print(A.shape)
print(C.shape)

# 순전파
X_dot_W = np.array([[0, 0, 0],[10, 10, 10]])
B = np.array([1, 2, 3])

print(X_dot_W)
print(X_dot_W + B)

# 역전파
dY = np.array([[1, 2, 3],[4, 5, 6]])
dB = np.sum(dY, axis=0)

print(dY)
print(dB)