# 5. Check student name

students = {"Amit", "Sneha", "Rahul", "Priya", "Riya"}

name = input("Enter student name: ")

if name in students:
    print("Student exists")
else:
    print("Student does not exist")