class Employee:
    def calculate_salary(self):
        print("Employee salary")


class Manager(Employee):
    def calculate_salary(self):
        basic = 50000
        bonus = 10000
        print("Manager Salary =", basic + bonus)


class Developer(Employee):
    def calculate_salary(self):
        basic = 40000
        bonus = 5000
        print("Developer Salary =", basic + bonus)


class Tester(Employee):
    def calculate_salary(self):
        basic = 30000
        bonus = 3000
        print("Tester Salary =", basic + bonus)


e = Manager()
e.calculate_salary()

e = Developer()
e.calculate_salary()

e = Tester()
e.calculate_salary()