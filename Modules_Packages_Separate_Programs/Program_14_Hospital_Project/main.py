# Program 14: Hospital Project Main Program

from patient.management import add_patient
from doctor.management import add_doctor
from billing.bill import calculate_bill
from medical_records.record import create_record

patient = add_patient("Amit", 20)
doctor = add_doctor("Dr. Sharma", "General Medicine")
bill = calculate_bill(500, 1200)
record = create_record("Amit", "Fever")

print("Patient =", patient)
print("Doctor =", doctor)
print("Bill =", bill)
print("Medical Record =", record)
