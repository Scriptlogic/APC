marks = {
    "Rahul": 75,
    "Priya": 82,
    "Amit": 68
}

name = input("Enter student name: ").capitalize()
new_marks = int(input("Enter new marks: "))

if name in marks:
    marks[name] = new_marks
    print("Updated dictionary:", marks)
else:
    print("Student not found")