from dal.Patient_repository import PatientRepository


class DoctorsListFlow:

    def get_all_doctors(self):
        return PatientRepository().get_all_doctors()

    def get_available_doctors(self):
        return PatientRepository().get_available_doctors()
