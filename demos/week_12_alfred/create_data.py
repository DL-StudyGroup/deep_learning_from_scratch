# coding: utf-8
import sys, os
import numpy as np
sys.path.append(os.pardir)


x = np.random.rand(10, 1, 28, 28)
print(x.shape)
print(x[0].shape)
print(x)