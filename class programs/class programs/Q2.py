class Employee:
    def __init__(self, emp_id, name, basic_salary):
        self.emp_id = emp_id
        self.name = name
        self.basic_salary = basic_salary

    def calculate(self):
        hra = 0.20 * self.basic_salary
        da = 0.10 * self.basic_salary
        gross_salary = self.basic_salary + hra + da

        print("Employee ID:", self.emp_id)
        print("Name:", self.name)
        print("Basic Salary:", self.basic_salary)
        print("HRA:", hra)
        print("DA:", da)
        print("Gross Salary:", gross_salary)


e = Employee(101, "Rohan", 30000)
e.calculate()