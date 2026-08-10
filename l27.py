salaries = [25000, 45000, 60000, 85000, 28000, 52000, 95000, 18000]

highest_sal = max(salaries)
lowest_sal = min(salaries)
avg_sal = sum(salaries) / len(salaries)

above_50k = [sal for sal in salaries if sal > 50000]
below_30k = [sal for sal in salaries if sal < 30000]

print("Highest Salary:", highest_sal)
print("Lowest Salary:", lowest_sal)
print("Average Salary:", round(avg_sal, 2))
print("Count earning above ₹50,000:", len(above_50k))
print("Count earning below ₹30,000:", len(below_30k))