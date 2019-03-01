import numpy as np

print("hello World...")
print("hello World...")

x = [[0, 1]]
# y = [[0], [1], [2]]
w = [[1, 3, 5], [2, 4, 6]]

x = np.int32(x)
# y = np.int32(y)
w = np.int32(w)

print(x)
print(x.shape)
# print(y.shape)
print(w.shape)

print(np.dot(x, w))
print(np.dot(x, w).shape)