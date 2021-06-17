from dal.Appointment_repository import AppointmentRepository
from dal.Inmemory_database import In_Memory_Database
from model.config_model import Patient


class PatientRepository:
    def __init__(self):
        self.db = In_Memory_Database
        self.appointment_data = AppointmentRepository()

    def get_all_doctors(self) -> str:
        return self.db.get_all_doctors()

    def get_available_doctors(self) -> str:
        return self.db.get_available_doctors()

    def add_appointment(self, patient: Patient) -> str:
        self.db.add(patient)

    def remove_appointment(self, patient: Patient) -> str:
        return self.db.remove_appointment(patient)

    def get_waiting_list(self) -> str:
        return self.appointment_data.get_sorted_waiting_patients_list()


