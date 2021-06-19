from dal.Patient_repository import PatientRepository
from model.config_model import Patient


class AddWaitingListFlow:
    def __init__(self, patient: Patient):
        self.patient_repository = PatientRepository()
        self.waiting_patient = patient

    def add_patient_to_waiting_list(self, patient: Patient):
        self.patient_repository.add_patient_to_waiting_list(patient)
        return self.waiting_patient
