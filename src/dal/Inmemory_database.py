from typing import List

from model.config_model import Patient, Doctor, Appointment


class InMemoryDatabase:
    def __init__(self):
        # our data base
        self.doctors_list = []
        self.patients_list = []
        self.appointments_list = []
        self.waiting_list = []

    def add_appointment(self, appointment: Appointment):
        self.appointments_list.append(appointment)

    def remove_appointment(self, appointment_id: int) -> str:
        patients_appointments_list = self.appointments_list
        appointment = list(filter(lambda m: appointment_id == appointment_id, patients_appointments_list))
        self.appointments_list.remove(appointment[0])
        return "Canceled!", 200

    def add_doctor(self, doctor: Doctor):
        self.doctors_list.append(doctor)

    def get_doctor_by_id(self, doctor_id: int):
        doctors_list = self.doctors_list
        doctor = list(filter(lambda m: m.doctor_id == doctor_id, doctors_list))
        result = doctor[0]
        return result

    def get_all_doctors(self) -> List[Doctor]:
        doctors = self.doctors_list
        return doctors

    def add_patient(self, patient: Patient):
        self.patients_list.append(patient)

    def add_patient_to_waiting_list(self, patient: Patient):
        self.doctors_waiting_list.append(patient)


In_Memory_Database = InMemoryDatabase()
