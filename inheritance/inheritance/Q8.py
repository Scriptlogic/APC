class Employee:
    def __init__(self, emp_id, name, basic_salary):
        self.emp_id = emp_id
        self.name = name
        self.basic_salary = basic_salary

    def display(self):
        print("Employee ID:", self.emp_id)
        print("Name:", self.name)
        print("Basic Salary:", self.basic_salary)


class Manager(Employee):
    def calculate_salary(self):
        allowance = self.basic_salary * 20 / 100
        return self.basic_salary + allowance


class Developer(Employee):
    def calculate_salary(self):
        allowance = self.basic_salary * 15 / 100
        return self.basic_salary + allowance


class Tester(Employee):
    def calculate_salary(self):
        allowance = self.basic_salary * 10 / 100
        return self.basic_salary + allowance


m = Manager(101, "Rahul", 50000)
d = Developer(102, "Amit", 40000)
t = Tester(103, "Sneha", 30000)

m.display()
print("Total Salary:", m.calculate_salary())

print()

d.display()
print("Total Salary:", d.calculate_salary())

print()

t.display()
print("Total Salary:", t.calculate_salary())
