from dal.inmemory_database import In_Memory_Database
from model.config_model import Patient


class WaitingListRepository:
    def __init__(self):
        self.db = In_Memory_Database

    def add_patient_to_waiting_list(self, patient: Patient):
        self.db.waiting_list.append(patient)
