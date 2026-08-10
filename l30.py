
patients = [
    ["John Doe", 45],
    ["Jane Smith", 30],
    ["Sam Brown", 60]
]

new_patient = ["Alice Green", 25]
patients.append(new_patient)
print("Added Patient. Current Patients:", patients)
remove_name = "Jane Smith"
patients = [p for p in patients if p[0] != remove_name]

print(f"Removed '{remove_name}'. Final Patient List:")
for name, age in patients:
    print(f"Name: {name}, Age: {age}")