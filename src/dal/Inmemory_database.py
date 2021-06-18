from typing import List

from model.config_model import Patient, Doctor, Appointment


class InMemoryDatabase:
    def __init__(self):
        # our data base
        self.doctors_list = []
        self.patients_list = []
        self.appointments_list = []
        self.available_doctors_list = []
        self.patients_waiting_list = []

    def add_appointment(self, appointment: Appointment):
        self.appointments_list.append(appointment)
        print(self.appointments_list)

    def remove_appointment(self, appointment: Appointment) -> str:
        return "Deleted!", 200

    def add_patient(self, patient: Patient):
        self.patients_list.append(patient)

    def add_doctor(self, doctor: Doctor):
        self.doctors_list.append(doctor)

    def get_doctor_by_id(self, doctor_id: int):
        doctors_list = self.doctors_list
        doctor = list(filter(lambda m: m.doctor_id == doctor_id, doctors_list))
        return doctor[0]

    def get_all_doctors(self) -> List[Doctor]:
        doctors = self.doctors_list
        return doctors

    def get_available_doctors(self) -> List[Doctor]:
        doctors = self.doctors_list
        available_doctors = None
        return available_doctors

    def get_waiting_patients(self) -> List[Patient]:
        return


In_Memory_Database = InMemoryDatabase()
