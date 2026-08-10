students = ["Alice", "Bob", "Charlie", "David"]
print("Total students present:", len(students))
search_name = "Bob"
if search_name in students:
    print(f"{search_name} is Present.")
else:
    print(f"{search_name} is Absent.")
students.append("Eve")
print("Added Eve. Updated list:", students)
absent_student = "Charlie"
if absent_student in students:
    students.remove(absent_student)
    print(f"Removed {absent_student}. Updated list:", students)