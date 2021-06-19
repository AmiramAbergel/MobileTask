from dal.Doctor_repository import DoctorRepository


class DoctorsListFlow:
    def __init__(self):
        self.doctor_repository = DoctorRepository()

    def get_all_doctors(self) -> str:
        return self.doctor_repository.get_all_doctors()
