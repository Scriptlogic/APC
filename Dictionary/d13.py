students = {
    "Rahul": 85,
    "Priya": 92,
    "Amit": 78,
    "Sneha": 88
}

total = 0

for marks in students.values():
    total = total + marks

average = total / len(students)

print("Average marks =", average)