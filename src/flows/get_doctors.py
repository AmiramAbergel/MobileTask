from dal.Doctor_repository import DoctorRepository


class DoctorsListFlow:

    def get_all_doctors(self) -> str:
        return DoctorRepository().get_all_doctors()
