import pandas as pd

salary = pd.Series({
    "Amit": 45000,
    "Priya": 60000,
    "Rahul": 55000,
    "Sneha": 75000,
    "Neha": 40000
})

print("Salary Series:")
print(salary)

print("\nHighest salary:", salary.max())
print("Lowest salary:", salary.min())
print("Average salary:", salary.mean())

print("\nEmployees earning more than 50000:")
print(salary[salary > 50000])