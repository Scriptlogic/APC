import pandas as pd

data = {
    "Employee_ID": [101, 102, 103, 104, 105],
    "Name": ["Amit", "Priya", "Rahul", "Sneha", "Neha"],
    "Department": ["CSE", "IT", "HR", "CSE", "Finance"],
    "Salary": [45000, 60000, 55000, 75000, 50000],
    "Experience": [2, 5, 4, 8, 3]
}

df = pd.DataFrame(data)

print("Employees with salary greater than 50000:")
print(df[df["Salary"] > 50000])

print("\nAverage Salary:", df["Salary"].mean())

print("Highest Salary:", df["Salary"].max())

print("\nEmployee with highest experience:")
print(df.loc[df["Experience"].idxmax()])