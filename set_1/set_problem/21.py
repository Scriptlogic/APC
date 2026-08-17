# 21. Find students enrolled in both and only one course

python_students = {"Amit", "Sneha", "Rahul", "Priya"}
java_students = {"Rahul", "Priya", "Riya", "Karan"}

both = python_students & java_students
only_one = python_students ^ java_students

print("Students enrolled in both:", both)
print("Students enrolled in only one course:", only_one)