from dal.inmemory_database import In_Memory_Database
from model.config_model import Doctor


class DoctorRepository:
    def __init__(self):
        self.db = In_Memory_Database

    def get_all_doctors(self) -> str:
        return self.db.doctors_list

    def add_doctor(self, doctor: Doctor):
        self.db.add_doctor(doctor)

    def get_doctor_by_id(self, doctor_id: int) -> Doctor:
        return self.db.get_doctor_by_id(doctor_id)

    def get_list_id_of_waiting_patients(self, doctor_id: int):
        doctor = self.get_doctor_by_id(doctor_id)
        doctor_waiting_list = doctor.waiting_patients_id
        return doctor_waiting_list



