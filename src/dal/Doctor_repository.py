from dal.Inmemory_database import In_Memory_Database
from model.config_model import Doctor


class DoctorRepository:
    def __init__(self):
        self.db = In_Memory_Database

    def get_all_doctors(self) -> str:
        return self.db.doctors_list

    def get_doctor_by_id(self, doctor_id: int) -> Doctor:
        return self.db.get_doctor_by_id(doctor_id)

