students = [
    ("Rahul", 80),
    ("Amit", 65),
    ("Sneha", 90),
    ("Priya", 78)
]

def average(students):
    total = sum(map(lambda x: x[1], students))
    return total / len(students)

print("Average =", average(students))

above_75 = list(filter(lambda x: x[1] > 75, students))
print("Above 75 =", above_75)

sorted_students = sorted(students, key=lambda x: x[1])
print("Sorted students =", sorted_students)