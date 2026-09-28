import pandas as pd

# Read CSV file
df = pd.read_csv("Pandas/patients.csv")

# Display complete data
print("Patient Details:")
print(df)

# Patients above 60 years
print("\nPatients above 60 years:")
print(df[df["Age"] > 60])

# Average medical expense
print("\nAverage Medical Expense:")
print(df["Medical_Expense"].mean())

# Patient with highest medical expense
print("\nPatient with Highest Medical Expense:")
print(df.loc[df["Medical_Expense"].idxmax()])

# Number of patients for each disease
print("\nNumber of Patients for Each Disease:")
print(df["Disease"].value_counts())

# Patients with medical expense greater than 50000
print("\nPatients with Medical Expense Greater Than 50000:")
print(df[df["Medical_Expense"] > 50000])