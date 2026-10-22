import numpy as np
# jose solis nc 1472 Array indexing in NumPy
j1472 = np.array([10, 20, 30, 40, 50])
print(j1472)
print(j1472[0])
print(j1472[3])
print(j1472[-1])
print(j1472[-2])
print("----------------------------------------")
j1472 = np.array([
    [10, 20, 30],
    [40, 50, 60]
])
print(j1472)
print(j1472[0, 0])
print(j1472[1, 2])
print(j1472[-1, -1])
print(j1472[-2, 2])
print("----------------------------------------")
# 3D array 2x2(2x3)
j1472 = np.array([
    # 0 -2
    [
        [10, 20, 30],
        [40, 50, 60]
    ],
    # 1 -1
    [
        [70, 80, 90],
        [100, 110, 120]
    ]
])
print(j1472)
print(j1472[0, 0, 0])
print(j1472[1, 1, 2])
print(j1472[-1, 1, -2])

print("jose solis nc 1472")