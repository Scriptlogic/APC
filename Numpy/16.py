import numpy as np

marks = np.array([75, 82, 65, 90, 55, 78, 88, 60, 72, 95])

print("Marks:", marks)

print("Highest marks:", np.max(marks))
print("Lowest marks:", np.min(marks))
print("Average marks:", np.mean(marks))
print("Median:", np.median(marks))
print("Standard deviation:", np.std(marks))