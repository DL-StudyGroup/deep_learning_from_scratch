# coding: utf-8
import numpy as np

arr = np.arange(48).reshape(2, 4, 6)
# arr = np.ones((2, 4, 6), dtype=int)
print(arr)

print(arr[0:2, 1:4, 0:4])

arr2 = np.zeros((2, 4, 6, 2), dtype=int)
# print(arr2)


# arr2[:, :, 0, :] = arr[:, :, 1:3]
# print(arr2[:, :, 0, :].shape)
# print(arr[:, :, 1:3].shape)
# print(arr2.shape)
# print(arr2)
print(range(5))
arr3 = np.zeros((2, 4, 6, 2, 2), dtype=int)
for y in range(4):
    for x in range(6):
        arr3[:, y, x, :, :] = arr[:, y:y + 2, x:x + 2]
        print("------------------")
        print(arr[:, y:y + 2, x:x + 2])
        print("y: ", y, "x: ", x)
        print(arr3)
        print(arr3.shape)
# print(arr3)

exit()
