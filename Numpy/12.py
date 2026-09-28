import numpy as np

arr = np.array([10, 60, 25, 80, 45, 90, 30, 55, 20, 70])

print("Original array:", arr)

arr[arr > 50] = 0

print("After replacing:", arr)