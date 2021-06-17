from dal.Appointment_repository import AppointmentRepository
from dal.Inmemory_database import In_Memory_Database


class DoctorRepository:
    def __init__(self):
        self.db = In_Memory_Database
        self.appointment_data = AppointmentRepository()

    def get_sorted_waiting_patients_list(self) -> str:
        return self.appointment_data.get_sorted_waiting_patients_list()
