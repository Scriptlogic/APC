def read_employees():
    file = open("employees.txt", "r")

    employees = []

    for line in file:
        emp_id, name, department, salary = line.strip().split(",")

        employee = {
            "id": emp_id,
            "name": name,
            "department": department,
            "salary": float(salary)
        }

        employees.append(employee)

    file.close()

    return employees


def display_employees(employees):
    print("All Employees:")

    for employee in employees:
        print(
            employee["id"],
            employee["name"],
            employee["department"],
            employee["salary"]
        )


def highest_paid(employees):
    employee = max(employees, key=lambda x: x["salary"])

    print("\nHighest Paid Employee:")
    print(employee["name"], "-", employee["salary"])


def average_salary(employees):
    total = 0

    for employee in employees:
        total += employee["salary"]

    average = total / len(employees)

    print("\nAverage Salary:", average)


def above_salary(employees, salary):
    print("\nEmployees earning above", salary, ":")

    for employee in employees:
        if employee["salary"] > salary:
            print(employee["name"], "-", employee["salary"])


employees = read_employees()

display_employees(employees)

highest_paid(employees)

average_salary(employees)

above_salary(employees, 50000)