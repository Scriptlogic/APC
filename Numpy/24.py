import numpy as np

arr = np.random.randint(1, 101, size=(3, 4, 5))

flat = arr.flatten()

print("3D Array:")
print(arr)

print("\nFlattened array:")
print(flat)

print("\nElements greater than 50:")
print(flat[flat > 50])

print("\nEven numbers:")
print(flat[flat % 2 == 0])

average = np.mean(flat)

print("\nAverage:", average)

print("Elements less than average:")
print(flat[flat < average])