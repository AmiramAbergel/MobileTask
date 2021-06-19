from typing import List

from dal.Inmemory_database import In_Memory_Database
from model.config_model import Patient


class PatientRepository:
    def __init__(self):
        self.db = In_Memory_Database

    def add_patient_to_waiting_list(self, patient: Patient):
        self.db.add_patient_to_waiting_list(patient)

    def get_waiting_list(self) -> List[Patient]:
        return self.db.waiting_list

