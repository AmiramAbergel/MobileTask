from dal.patient_repository import PatientRepository
from model.config_model import Patient


class AddPatientFlow:
    def __init__(self, patient: Patient):
        self.patient_repository = PatientRepository()
        self.new_patient = patient

    def add_patient(self) -> Patient:
        self.patient_repository.add_patient(self.new_patient)
        return self.new_patient
