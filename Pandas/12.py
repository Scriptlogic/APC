import pandas as pd

attendance = pd.Series({
    "Amit": 92,
    "Priya": 85,
    "Rahul": 70,
    "Sneha": 95,
    "Neha": 68
})

print("Average attendance:")
print(attendance.mean())

print("\nStudents below 75%:")
print(attendance[attendance < 75])

print("\nStudents above 90%:")
print(attendance[attendance > 90])

print("\nHighest attendance:")
print(attendance.max())