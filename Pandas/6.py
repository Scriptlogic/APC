import pandas as pd

data = {
    "Student_ID": [1, 2, 3, 4, 5],
    "Name": ["Amit", "Priya", "Rahul", "Sneha", "Neha"],
    "Department": ["CSE", "IT", "CSE", "ECE", "CSE"],
    "Total_Classes": [100, 100, 100, 100, 100],
    "Classes_Attended": [90, 70, 80, 65, 95]
}

df = pd.DataFrame(data)

df["Attendance_Percentage"] = (
    df["Classes_Attended"] / df["Total_Classes"]
) * 100

print(df)

print("\nStudents with attendance below 75%:")
print(df[df["Attendance_Percentage"] < 75])