# Program 2: Main Program for Student Result Module

import student

marks = []
for i in range(5):
    marks.append(float(input("Enter marks: ")))

total = student.total_marks(marks)
percent = student.percentage(marks)

print("Total =", total)
print("Percentage =", percent)
print("Grade =", student.grade(percent))
