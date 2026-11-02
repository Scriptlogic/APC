# Program 5: Employee Salary Module

def gross_salary(basic):
    hra = basic * 0.20
    da = basic * 0.10
    return basic + hra + da

def deductions(gross):
    return gross * 0.10

def net_salary(basic):
    gross = gross_salary(basic)
    return gross - deductions(gross)
