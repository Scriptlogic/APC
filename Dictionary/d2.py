employee = {
    "ID": 101,
    "Name": "Rahul",
    "Department": "IT",
    "Salary": 30000
}

key = input("Enter key: ")

if key in employee:
    print("Value:", employee[key])
else:
    print("Key not found")