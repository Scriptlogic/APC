marks = [78, 85, 92, 45, 60, 88, 90, 34, 55, 67, 72, 81, 95, 40, 50, 63, 77, 84, 89, 91]

highest = max(marks)
lowest = min(marks)
avg_marks = sum(marks) / len(marks)

above_avg = sum(1 for m in marks if m > avg_marks)
below_avg = sum(1 for m in marks if m < avg_marks)

print("Highest Marks:", highest)
print("Lowest Marks:", lowest)
print("Average Marks:", round(avg_marks, 2))
print("Students Above Average:", above_avg)
print("Students Below Average:", below_avg)