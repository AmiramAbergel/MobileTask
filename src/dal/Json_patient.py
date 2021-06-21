import json
from dal.Patient_repository import PatientRepository
from model.config_model import Patient


class JsonPatient:
    def __init__(self, patient: Patient):
        self.patient_repository = PatientRepository()
        self.patient = patient

    def read_and_create(self):
        patient_data = [
            {
                "Patient-ID": self.patient.patient_id,
                "Patient-Name": self.patient.patient_full_name,
                "Doctor-Name": self.patient.doctor_full_name,
                "Patient-Phone": self.patient.patient_phone,
                "Patient-Message": self.patient.patient_message,
                "Patient-Waiting-Status": self.patient.patient_waiting_status
            }
        ]

        with open('local_json/PatientData.json', 'w') as outfile:
            json.dump(patient_data, outfile)


