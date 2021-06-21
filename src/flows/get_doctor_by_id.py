from dal.Doctor_repository import DoctorRepository
from model.config_model import Doctor


class GetDoctorByIdFlow:
    def __init__(self, doctor_id: int):
        self.doctor_id = doctor_id
        self.doctor_repository = DoctorRepository()

    def get_doctor_by_id(self) -> Doctor:
        doctor = self.doctor_repository.get_doctor_by_id(self.doctor_id)
        return doctor

