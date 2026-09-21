from abc import ABC, abstractmethod

class Patient(ABC):

    @abstractmethod
    def calculate_bill(self):
        pass

    @abstractmethod
    def treatment(self):
        pass


class InPatient(Patient):
    def calculate_bill(self):
        print("InPatient Bill = 5000")

    def treatment(self):
        print("InPatient receives hospital treatment")


class OutPatient(Patient):
    def calculate_bill(self):
        print("OutPatient Bill = 1000")

    def treatment(self):
        print("OutPatient receives consultation")


class EmergencyPatient(Patient):
    def calculate_bill(self):
        print("Emergency Patient Bill = 10000")

    def treatment(self):
        print("Emergency Patient receives emergency treatment")


p1 = InPatient()
p1.calculate_bill()
p1.treatment()

p2 = OutPatient()
p2.calculate_bill()
p2.treatment()

p3 = EmergencyPatient()
p3.calculate_bill()
p3.treatment()