from typing import List

from model.config_model import Patient, Doctor


class InMemoryDatabase:
    def __init__(self):
        # our data base
        self.doctors_list = []
        self.available_doctors_list = []
        self.appointment_list = []
        self.patients_waiting_list = []

    def add(self, patient: Patient):
        self.appointment_list.append(patient)

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
