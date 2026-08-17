students = {
    "Rahul": 85,
    "Priya": 92,
    "Amit": 78,
    "Sneha": 88
}

highest = 0
name = ""

for student, marks in students.items():
    if marks > highest:
        highest = marks
        name = student

print("Highest marks:", highest)
print("Student:", name)