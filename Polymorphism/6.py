class Student:
    def calculate_grade(self):
        print("Student grade")


class EngineeringStudent(Student):
    def calculate_grade(self):
        marks = 85

        if marks >= 75:
            print("Engineering Student: Distinction")
        elif marks >= 60:
            print("Engineering Student: First Class")
        else:
            print("Engineering Student: Pass")


class MedicalStudent(Student):
    def calculate_grade(self):
        marks = 70

        if marks >= 70:
            print("Medical Student: Distinction")
        elif marks >= 60:
            print("Medical Student: First Class")
        else:
            print("Medical Student: Pass")


class ManagementStudent(Student):
    def calculate_grade(self):
        marks = 65

        if marks >= 80:
            print("Management Student: A Grade")
        elif marks >= 60:
            print("Management Student: B Grade")
        else:
            print("Management Student: C Grade")


s = EngineeringStudent()
s.calculate_grade()

s = MedicalStudent()
s.calculate_grade()

s = ManagementStudent()
s.calculate_grade()