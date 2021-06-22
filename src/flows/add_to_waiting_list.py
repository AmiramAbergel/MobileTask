from dal.patient_repository import PatientRepository
from dal.waiting_list_repository import WaitingListRepository
from model.config_model import Patient


class AddWaitingListFlow:
    def __init__(self, patient: Patient):
        self.waiting_list_repository = WaitingListRepository()
        self.waiting_patient = patient

    def add_patient_to_waiting_list(self) -> Patient:
        self.waiting_list_repository.add_patient_to_waiting_list(self.waiting_patient)
        return self.waiting_patient
