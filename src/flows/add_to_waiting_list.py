from dal.Patient_repository import PatientRepository
from model.config_model import Patient


class AddWaitingListFlow:
    def __init__(self):
        self.patient_repository = PatientRepository()

    def add_patient_to_waiting_list(self, patient_id: int, patient_full_name: str, patient_phone: str,
                                    patient_message: str, patient_waiting_status: str):
        patient = Patient(patient_id, patient_full_name, patient_phone, patient_message, patient_waiting_status)
        self.patient_repository.add_patient_to_waiting_list(patient)
        return patient
