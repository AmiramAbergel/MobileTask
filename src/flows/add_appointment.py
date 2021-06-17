from dal.Patient_repository import PatientRepository
from model.config_model import Patient


class AddAppointmentFlow:
    def add(self, patient_id: int, patient_full_name: str, patient_phone: str, patient_message: str, patient_arrival_time: str, patient_waiting_status: str):
        patient = Patient(patient_id, patient_full_name, patient_phone, patient_message, patient_arrival_time, patient_waiting_status)
        PatientRepository().add_appointment(patient)
        return patient
