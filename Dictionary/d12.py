students = {
    "Rahul": 85,
    "Priya": 92,
    "Amit": 78,
    "Sneha": 88
}

lowest = 999
name = ""

for student, marks in students.items():
    if marks < lowest:
        lowest = marks
        name = student

print("Lowest marks:", lowest)
print("Student:", name)