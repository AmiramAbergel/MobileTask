from typing import List

from dal.Patient_repository import PatientRepository
from model.config_model import Patient


class PatientsListFlow:
    def __init__(self):
        self.patient_repository = PatientRepository()

    def get_all_patients(self) -> List[Patient]:
        return self.patient_repository.get_patients_list()
