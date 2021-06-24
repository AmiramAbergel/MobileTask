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

    def get_patients_by_arrival_time(self, patient_arrival) -> Patient:
        return self.db.get_patient_by_arrival_time(patient_arrival)

    def remove_patient_by_id(self, patient_id: int) -> str:
        return self.db.remove_patient_by_id(patient_id)

