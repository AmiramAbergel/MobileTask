from datetime import datetime
from typing import List

from dal.Patient_repository import PatientRepository
from model.config_model import Patient


class SortedWaitingListFlow:
    def __init__(self):
        self.patient_repository = PatientRepository()

    def get_sorted_waiting_list(self) -> List[Patient]:
        waiting_list = self.patient_repository.get_patients_list()
        waiting_list.sort(key=lambda date: datetime.strptime(date.patient_arrival_time, "%Y-%m-%d %H:%M:%S"))
        return waiting_list
