# coding: utf-8
import numpy as np

arr = np.arange(48).reshape(2, 4, 6)
print("-------------------")
print("arr:")
print(arr)
print("-------------------")

t1 = arr.transpose(0, 1, 2)
print("-------------------")
print("t1: 0, 1, 2")
print(t1)
print("-------------------")

t2 = arr.transpose(1, 0, 2)
print("-------------------")
print("t2: 1, 0, 2")
print(t2)
print("-------------------")

t3 = arr.transpose(0, 2, 1)

print("-------------------")
print("t3: 0, 2, 1")
print(t3)
print("-------------------")

# col = np.zeros((N, C, filter_h, filter_w, out_h, out_w))
# col = col.transpose(0, 4, 5, 1, 2, 3).reshape(N * out_h * out_w, -1)
# (N, out_h, out_w, C, filter_h, filter_w)