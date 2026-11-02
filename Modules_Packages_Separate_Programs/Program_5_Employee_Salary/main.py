# Program 5: Main Program for Employee Salary Module

import salary

basic = float(input("Enter basic salary: "))

gross = salary.gross_salary(basic)
deduction = salary.deductions(gross)
net = salary.net_salary(basic)

print("Gross Salary =", gross)
print("Deductions =", deduction)
print("Net Salary =", net)
