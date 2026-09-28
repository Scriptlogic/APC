import numpy as np

a = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

b = np.array([
    [7, 8],
    [9, 10],
    [11, 12]
])

result = np.matmul(a, b)

print("Matrix A:")
print(a)

print("\nMatrix B:")
print(b)

print("\nMatrix Multiplication:")
print(result)