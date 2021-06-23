import json

from flask import request

from dal.patient_repository import PatientRepository
from model.config_model import Patient


class ValidatePatientFlow:
    def __init__(self, patient_id: int):
        self.patient_id = patient_id
        self.patient_repository = PatientRepository()
        self.patient_list = self.patient_repository.get_patients_list()

    def check_existing_by_id(self):
        for patient in self.patient_list:
            if self.patient_id == patient.patient_id:
                return True
            else:
                self.create_and_append_patient()

    def create_and_append_patient(self):
        request_data = request.get_data()
        data = json.loads(request_data)
        patient_id = data.get('Patient-ID')
        patient_name = data.get('Patient-Name')
        doctor_name = data.get('Doctor-Name')
        patient_phone = data.get('Patient-Phone')
        patient_message = data.get('Patient-Message')
        patient_waiting_status = data.get('Patient-Waiting-Status')

        patient_obj = Patient(patient_id, patient_name, doctor_name, patient_phone, patient_message,
                              patient_waiting_status)
        self.db.add_patient(patient_obj)
        print("----------------------Patient added successfully----------------------")
        return self.db.patients_list
