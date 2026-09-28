import pandas as pd

marks = pd.Series({
    "Amit": 80,
    "Priya": 90,
    "Rahul": 65,
    "Sneha": 75,
    "Neha": 85
})

print("Series:")
print(marks)

print("\nMarks of Priya:")
print(marks["Priya"])

print("\nMaximum marks:", marks.max())
print("Minimum marks:", marks.min())
print("Average marks:", marks.mean())

print("\nStudents scoring more than 75:")
print(marks[marks > 75])