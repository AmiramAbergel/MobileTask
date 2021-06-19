from typing import List
from datetime import datetime

from dal.Patient_repository import PatientRepository
from model.config_model import Patient


class WaitingListFlow:
    def __init__(self):
        self.patient_repository = PatientRepository()
        self.waiting_list = self.patient_repository.get_waiting_list()

    def get_waiting_list(self) -> List[Patient]:
        return self.waiting_list

    def get_sorted_waiting_list(self) -> List[Patient]:
        waiting_list = self.patient_repository.get_patients_list()
        waiting_list.sort(key=lambda date: datetime.strptime(date.patient_arrival_time, "%Y-%m-%d %H:%M:%S.%f"))
        return waiting_list
