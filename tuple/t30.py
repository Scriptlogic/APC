patients = (
    (101, "Rahul", 25, "A+"),
    (102, "Priya", 30, "B+"),
    (103, "Amit", 40, "O+"),
    (104, "Sneha", 28, "A+")
)

print("All Patient Records:")

for patient in patients:
    print(patient)


id = int(input("\nEnter Patient ID: "))

found = False

for patient in patients:
    if patient[0] == id:
        print("Patient Found:", patient)
        found = True

if found == False:
    print("Patient not found")


print("Total Patients =", len(patients))

group = input("\nEnter Blood Group: ")

print("Patients with", group, "blood group:")

for patient in patients:
    if patient[3] == group:
        print(patient)