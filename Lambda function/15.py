students = [
    ("Rahul", 85),
    ("Amit", 70),
    ("Sneha", 95),
    ("Priya", 80)
]

result = sorted(students, key=lambda x: x[1])

print("Students =", result)