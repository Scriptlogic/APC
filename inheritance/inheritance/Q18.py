class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_person(self):
        print("Name:", self.name)
        print("Age:", self.age)


class Doctor(Person):
    def __init__(self, name, age, doctor_id):
        super().__init__(name, age)
        self.doctor_id = doctor_id

    def display_doctor(self):
        print("Doctor ID:", self.doctor_id)


class Patient(Person):
    def __init__(self, name, age, patient_id):
        super().__init__(name, age)
        self.patient_id = patient_id

    def display_patient(self):
        print("Patient ID:", self.patient_id)


class Surgeon(Doctor):
    def __init__(self, name, age, doctor_id, specialization):
        super().__init__(name, age, doctor_id)
        self.specialization = specialization

    def display_surgeon(self):
        self.display_person()
        self.display_doctor()
        print("Specialization:", self.specialization)


class MedicalResearcher(Doctor, Patient):
    def __init__(self, name, age, doctor_id, patient_id, research_area):
        Person.__init__(self, name, age)
        self.doctor_id = doctor_id
        self.patient_id = patient_id
        self.research_area = research_area

    def display_researcher(self):
        self.display_person()
        print("Doctor ID:", self.doctor_id)
        print("Patient ID:", self.patient_id)
        print("Research Area:", self.research_area)


s = Surgeon("Dr. Rahul", 35, 101, "Cardiology")
m = MedicalResearcher("Dr. Amit", 40, 102, 202, "Cancer Research")

print("Surgeon Details")
s.display_surgeon()

print()

print("Medical Researcher Details")
m.display_researcher()