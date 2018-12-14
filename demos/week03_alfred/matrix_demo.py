import numpy as np

arrays = [
    np.array([1, 2, 3, 4]),

    np.array([
        [1, 2],
        [1, 0],
        [1, 1]
    ]),

    np.array([
        [1, 2, 3, 4],
        [1, 2, 3, 4],
        [1, 2, 3, 4],
        [1, 2, 3, 4],
        [1, 2, 3, 4]
    ]),

    np.array([
        [1, 2, 3, 4, 5],
        [1, 2, 3],
        [1, 2]
    ])
]

print("============")
for arr in arrays:
    print(np.ndim(arr))
    print(np.shape(arr))
    print(arr.shape)
    print("------------")
