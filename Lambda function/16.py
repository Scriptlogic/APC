employees = [
    ("Rahul", 50000),
    ("Amit", 40000),
    ("Sneha", 70000),
    ("Priya", 60000)
]

result = sorted(employees, key=lambda x: x[1])

print("Employees =", result)