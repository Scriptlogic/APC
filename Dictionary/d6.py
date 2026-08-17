employees = {
    101: "Rahul",
    102: "Priya",
    103: "Amit",
    104: "Sneha"
}

id = int(input("Enter Employee ID: "))

if id in employees:
    print("Employee ID exists")
else:
    print("Employee ID does not exist")