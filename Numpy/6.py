import numpy as np

a = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

b = np.array([
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
])

result = a + b

print("Matrix A:")
print(a)

print("\nMatrix B:")
print(b)

print("\nMatrix Addition:")
print(result)