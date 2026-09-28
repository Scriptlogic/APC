import numpy as np

arr = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
])

print("Matrix:")
print(arr)

print("\nSum of each row:")
print(np.sum(arr, axis=1))

print("\nSum of each column:")
print(np.sum(arr, axis=0))