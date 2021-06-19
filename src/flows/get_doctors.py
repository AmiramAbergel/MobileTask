from typing import List

from dal.Doctor_repository import DoctorRepository
from model.config_model import Doctor


class DoctorsListFlow:
    def __init__(self):
        self.doctor_repository = DoctorRepository()

    def get_all_doctors(self) -> List[Doctor]:
        return self.doctor_repository.get_all_doctors()
