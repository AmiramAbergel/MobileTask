from dal.Patient_repository import PatientRepository


class GetPatientByIdFlow:
    def __init__(self, patient_id: int):
        self.patient_id = patient_id
        self.patient_repository = PatientRepository()

    def get_patient_by_id(self, patient_id: int):
        patient = self.patient_repository.get_patient_by_id(patient_id)
        return patient
