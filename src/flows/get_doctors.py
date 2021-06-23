from typing import List

from dal.doctor_repository import DoctorRepository
from model.config_model import Doctor


class DoctorsListFlow:
    def __init__(self, doctor_id: int):
        self.doctor_id = doctor_id
        self.doctor_repository = DoctorRepository()
        self.available_doctors = []

    def get_all_doctors(self) -> List[Doctor]:
        return self.doctor_repository.get_all_doctors()

    def get_doctor_by_id(self) -> Doctor:
        doctor = self.doctor_repository.get_doctor_by_id(self.doctor_id)
        return doctor

    def get_available_doctors(self) -> List[Doctor]:
        doctors_list_data = self.doctor_repository.get_all_doctors()
        for doctor in doctors_list_data:
            if doctor.doctor_available_status:
                self.available_doctors.append(doctor)
        return self.available_doctors


