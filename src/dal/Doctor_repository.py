from dal.Appointment_repository import AppointmentRepository
from dal.Inmemory_database import In_Memory_Database
from model.config_model import Doctor


class DoctorRepository:
    def __init__(self):
        self.db = In_Memory_Database
        self.appointment_repository = AppointmentRepository()

    def get_all_doctors(self) -> str:
        return self.db.doctors_list

    def get_available_doctors(self) -> str:
        return self.db.available_doctors_list

    def get_doctor_by_id(self, doctor_id: int):
        return self.db.get_doctor_by_id(doctor_id)

    def get_sorted_waiting_patients_list(self) -> str:
        return self.appointment_repository.get_sorted_waiting_patients_list()
