from dal.patient_repository import PatientRepository


class DeletePatientByIdFlow:
    def __init__(self, patient_id: int):
        self.patient_id = patient_id
        self.patient_repository = PatientRepository()

    def remove_patient(self) -> str:
        return self.patient_repository.remove_patient_by_id(self.patient_id)
