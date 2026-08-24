def gross_salary(basic):
    hra = basic * 20 / 100
    da = basic * 10 / 100

    gross = basic + hra + da

    return gross

basic = float(input("Enter basic salary: "))

print("Gross Salary =", gross_salary(basic))