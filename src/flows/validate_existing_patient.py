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
        Name = input("Enter patient name                      : ")
        DoctorName = input("Enter name of doctor following the case : ")
        patient_phone = input("Enter patient age                       : ")
        patient_message = input("Enter patient message                    : ")
        res_patient = Patient(self.patient_id, Name, DoctorName, patient_phone, patient_message)
        self.patient_repository.add_patient(res_patient)
        print("----------------------Patient added successfully----------------------")








