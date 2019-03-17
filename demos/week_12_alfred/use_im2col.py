# coding: utf-8
import sys
import os
import numpy as np

sys.path.append(os.pardir)
from common.util import im2col

x1 = np.random.rand(1, 1, 4, 4)
col1 = im2col(x1, 2, 2, 1, 0)
print(col1.shape)

x3 = np.random.rand(1, 1, 7, 7)
col3 = im2col(x3, 5, 5, 1, 0)
print(col3.shape)

x4 = np.random.rand(1, 3, 7, 7)
col4 = im2col(x4, 5, 5, 1, 0)
print(col4.shape)

x2 = np.random.rand(10, 1, 4, 4)
# col2 = im2col(x2, 5, 5, 1, 0)
col2 = im2col(x2, 2, 2, 1, 0)
print(col2.shape)
