# coding: utf-8
import numpy as np

# 배열 내부구조를 명확하게 관찰하기 위해 연속된 값을 준비한다
# 연속된 값을 다차원배열에 차곡차곡 쌓아둠
arr = np.arange(1, 49).reshape(2, 4, 6)
print(arr)

# 배열내부에서 범위 추출   : 사용법
print(arr[:, 1:3, 0])

# 다차원 빈값배열 만들어 놈
arr2 = np.zeros((2, 4, 6, 2), dtype=int)
# print(arr2)

# 차원이 다른 배열의 값
print(arr2[:, :, 0, :])
arr2[:, :, 0, :] = arr[:, :, 1:5:2]
print(arr2)
print(arr[:, :, 1:3])

arr3 = np.zeros((2, 4, 6, 2, 2), dtype=int)
for y in range(4):
    for x in range(6):
        arr3[:, y, x, :, :] = arr[:, y:y+2, x:x+2]

print(arr3)
