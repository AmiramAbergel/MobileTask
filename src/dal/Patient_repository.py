from typing import List

from dal.Inmemory_database import In_Memory_Database
from model.config_model import Patient


class PatientRepository:
    def __init__(self):
        self.db = In_Memory_Database

    def get_patients_list(self) -> List[Patient]:
        return self.db.patients_list

    def get_patient_by_id(self, patient_id: int):
        return self.db.get_patient_by_id(patient_id)

    def add_patient_to_waiting_list(self, patient: Patient):
        self.db.add_patient_to_waiting_list(patient)

    def get_waiting_list(self) -> List[Patient]:
        return self.db.waiting_list

