employees = [
    ("Rahul", "IT", 60000),
    ("Amit", "HR", 45000),
    ("Sneha", "IT", 75000),
    ("Priya", "Sales", 50000)
]

high_salary = list(filter(lambda x: x[2] > 50000, employees))
print("Salary above 50000 =", high_salary)

increased = list(map(lambda x: (x[0], x[1], x[2] * 1.10), employees))
print("Increased salaries =", increased)

sorted_employees = sorted(employees, key=lambda x: x[2])
print("Sorted employees =", sorted_employees)