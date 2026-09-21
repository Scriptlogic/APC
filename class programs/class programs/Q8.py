class Patient:
    def __init__(self, patient_id, name, age, disease, consultation_fee):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.disease = disease
        self.consultation_fee = consultation_fee

    def display(self):
        print("Patient ID:", self.patient_id)
        print("Name:", self.name)
        print("Age:", self.age)
        print("Disease:", self.disease)
        print("Consultation Fee:", self.consultation_fee)

    def total_bill(self):
        medicine = 500
        tests = 1000
        total = self.consultation_fee + medicine + tests
        print("Total Bill:", total)


p = Patient(101, "Amit", 25, "Fever", 500)

p.display()
p.total_bill()