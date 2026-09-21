class StudentResult:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def calculate_total(self):
        return sum(self.marks)

    def calculate_percentage(self):
        return self.calculate_total() / 5

    def calculate_grade(self):
        percentage = self.calculate_percentage()

        if percentage >= 90:
            return "A+"
        elif percentage >= 80:
            return "A"
        elif percentage >= 70:
            return "B"
        elif percentage >= 60:
            return "C"
        elif percentage >= 50:
            return "D"
        else:
            return "F"

    def display(self):
        print("Student Name:", self.name)
        print("Marks:", self.marks)
        print("Total Marks:", self.calculate_total())
        print("Percentage:", self.calculate_percentage(), "%")
        print("Grade:", self.calculate_grade())

    def __del__(self):
        print("StudentResult object destroyed.")


s = StudentResult("Sanjay", [85, 90, 78, 88, 92])

s.display()

del s