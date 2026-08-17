students = {}

for i in range(5):
    name = input("Enter student name: ")
    marks = int(input("Enter marks: "))
    students[name] = marks

print("Student Dictionary:")

for name, marks in students.items():
    print(name, ":", marks)