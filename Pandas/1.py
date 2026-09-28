import pandas as pd

data = {
    "Student_ID": [101, 102, 103, 104, 105],
    "Name": ["Amit", "Priya", "Rahul", "Sneha", "Neha"],
    "Python": [80, 70, 90, 85, 75],
    "DBMS": [75, 80, 85, 90, 70],
    "Maths": [85, 75, 80, 88, 78]
}

df = pd.DataFrame(data)

print("DataFrame:")
print(df)

df["Total"] = df["Python"] + df["DBMS"] + df["Maths"]
df["Average"] = df["Total"] / 3

print("\nDataFrame with Total and Average:")
print(df)

print("\nStudents with average greater than 75:")
print(df[df["Average"] > 75])