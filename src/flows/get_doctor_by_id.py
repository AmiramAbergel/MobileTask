from dal.Doctor_repository import DoctorRepository


class GetDoctorByIdFlow:
    def __init__(self, doctor_id: int):
        self.doctor_id = doctor_id
        self.doctor_repository = DoctorRepository()

    def get_doctor(self, doctor_id: int):
        doctor = self.doctor_repository.get_doctor_by_id(doctor_id)

        return doctor
