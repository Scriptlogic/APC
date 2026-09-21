from abc import ABC, abstractmethod

class Appointment(ABC):

    @abstractmethod
    def book_appointment(self):
        pass

    @abstractmethod
    def calculate_fee(self):
        pass


class GeneralAppointment(Appointment):
    def book_appointment(self):
        print("General Appointment Booked")

    def calculate_fee(self):
        print("General Appointment Fee = 500")


class SpecialistAppointment(Appointment):
    def book_appointment(self):
        print("Specialist Appointment Booked")

    def calculate_fee(self):
        print("Specialist Appointment Fee = 1000")


class EmergencyAppointment(Appointment):
    def book_appointment(self):
        print("Emergency Appointment Booked")

    def calculate_fee(self):
        print("Emergency Appointment Fee = 2000")


a1 = GeneralAppointment()
a1.book_appointment()
a1.calculate_fee()

a2 = SpecialistAppointment()
a2.book_appointment()
a2.calculate_fee()

a3 = EmergencyAppointment()
a3.book_appointment()

a3.calculate_fee()