from typing import List

from dal.inmemory_database import In_Memory_Database
from model.config_model import Patient


class PatientRepository:
    def __init__(self):
        self.db = In_Memory_Database

    def get_patients_list(self) -> List[Patient]:
        return self.db.patients_list

    def add_patient(self, patient: Patient):
        self.db.add_patient(patient)

    def get_patient_by_id(self, patient_id: int) -> Patient:
        return self.db.get_patient_by_id(patient_id)

    def add_patient_to_waiting_list(self, patient: Patient):
        self.db.add_patient_to_waiting_list(patient)

    def remove_patient_by_id(self, patient_id: int) -> str:
        return self.db.remove_patient_by_id(patient_id)

    def get_waiting_list(self) -> List[Patient]:
        return self.db.waiting_list

