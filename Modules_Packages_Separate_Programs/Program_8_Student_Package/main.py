# Program 8: Main Program for Student Package

from student.marks import total, percentage
from student.grade import calculate_grade
from student.attendance import attendance_percentage, eligible

marks = [80, 75, 90, 85, 70]

percent = percentage(marks)

print("Total =", total(marks))
print("Percentage =", percent)
print("Grade =", calculate_grade(percent))
print("Attendance =", attendance_percentage(80, 100))
print("Eligible =", eligible(80, 100))
