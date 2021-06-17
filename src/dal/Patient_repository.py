from dal.inmemory_database import In_Memory_Database
from model.config_model import Patient


class PatientRepository:
    def __init__(self):
        self.db = In_Memory_Database

    def get_all_doctors(self) -> str:
        return self.db.get_all_doctors()

    def get_available_doctors(self) -> str:
        return self.db.get_available_doctors()

    def add_appointment(self, patient: Patient) -> str:
        self.db.add(patient)

    def remove_appointment(self, patient: Patient) -> str:
        self.db.remove_appointment(patient)


