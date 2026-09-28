import numpy as np

marks = np.array([
    65, 78, 45, 90, 82,
    55, 72, 88, 60, 95,
    70, 84, 50, 76, 91,
    68, 73, 80, 59, 86
])

average = np.mean(marks)

print("Marks:", marks)
print("Class average:", average)

above_average = marks[marks > average]

print("Marks above average:", above_average)