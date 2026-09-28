import numpy as np

arr = np.random.randint(1, 101, size=(2, 3, 4))

print("Original array:")
print(arr)

arr[arr > 50] = 0

print("After replacing values greater than 50:")
print(arr)