import numpy as np

arr = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
])

print("Matrix:")
print(arr)

print("\nFirst row:")
print(arr[0])

print("\nLast column:")
print(arr[:, -1])

print("\nDiagonal elements:")
print(np.diag(arr))

print("\nSecond and third rows:")
print(arr[1:3])