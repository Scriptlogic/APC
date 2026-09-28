import pandas as pd

df = pd.read_csv("Pandas/employees.csv")

print("Employees from CSE department:")
print(df[df["Department"] == "CSE"])

print("\nAverage Salary:")
print(df["Salary"].mean())

print("\nHighest Salary:")
print(df["Salary"].max())

print("\nLowest Salary:")
print(df["Salary"].min())

print("\nEmployees with salary greater than 50000:")
print(df[df["Salary"] > 50000])

print("\nDepartment-wise Average Salary:")
print(df.groupby("Department")["Salary"].mean())