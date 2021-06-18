from typing import List

from model.config_model import Patient, Doctor


class InMemoryDatabase:
    def __init__(self):
        # our data base
        self.doctors_list = []
        self.patients_list = []
        self.appointments_list = []
        self.available_doctors_list = []
        self.patients_waiting_list = []

    def add_appointment(self, patient: Patient):
        self.appointments_list.append(patient)

    def add_patient(self, patient: Patient):
        self.patients_list.append(patient)

    def add_doctor(self, patient: Patient):
        self.doctors_list.append(patient)

    def get_all_doctors(self) -> List[Doctor]:
        doctors = self.doctors_list
        return doctors

    def get_available_doctors(self) -> List[Doctor]:
        doctors = self.doctors_list
        available_doctors = None
        return available_doctors

    def get_waiting_patients(self) -> List[Patient]:
        return

    def remove_appointment(self, patient: Patient) -> str:
        patients_appointment_list = self.appointment_list
        self.appointment_list.remove()
        print(self.appointment_list)
        return "Deleted!", 200


In_Memory_Database = InMemoryDatabase()
