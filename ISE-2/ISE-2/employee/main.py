import salary

name = input("Enter employee name: ")
basic_salary = float(input("Enter basic salary: "))
bonus = float(input("Enter bonus: "))
deduction = float(input("Enter deduction: "))

net_salary = salary.calculate_salary(basic_salary, bonus, deduction)

print("\nEmployee Name:", name)
print("Basic Salary:", basic_salary)
print("Bonus:", bonus)
print("Deduction:", deduction)
print("Net Salary:", net_salary)

