import numpy as np

arr = np.array([50, 20, 80, 10, 40, 70, 30])

print("Original array:", arr)

print("Ascending order:", np.sort(arr))
print("Descending order:", np.sort(arr)[::-1])