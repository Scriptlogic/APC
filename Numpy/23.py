import numpy as np

arr = np.arange(1, 25).reshape(2, 3, 4)

print("Original 3D array:")
print(arr)

flat = arr.flatten()

print("Flattened array:")
print(flat)