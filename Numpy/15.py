import numpy as np

a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])

print("Array A:")
print(a)

print("Array B:")
print(b)

print("Horizontal concatenation:")
print(np.hstack((a, b)))

print("Vertical concatenation:")
print(np.vstack((a, b)))