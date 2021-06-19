from typing import List
from dal.Patient_repository import PatientRepository
from model.config_model import Patient


class WaitingListFlow:
    def __init__(self):
        self.patient_repository = PatientRepository()

    def get_waiting_list(self) -> List[Patient]:
        return self.patient_repository.get_waiting_list()


