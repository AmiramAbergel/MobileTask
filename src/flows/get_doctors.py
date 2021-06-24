from datetime import datetime
from typing import List

from dal.doctor_repository import DoctorRepository
from dal.patient_repository import PatientRepository
from model.config_model import Doctor, Patient


class DoctorsListFlow:
    def __init__(self):
        self.doctor_repository = DoctorRepository()
        self.patient_repository = PatientRepository()
        self.available_doctors = []
        self.list_of_patients_info_by_id = []

    def get_all_doctors(self) -> List[Doctor]:
        return self.doctor_repository.get_all_doctors()

    def get_doctor_by_id(self, doctor_id: int) -> Doctor:
        doctor = self.doctor_repository.get_doctor_by_id(doctor_id)
        return doctor

    def get_available_doctors(self) -> List[Doctor]:
        doctors_list_data = self.doctor_repository.get_all_doctors()
        for doctor in doctors_list_data:
            if doctor.doctor_available_status:
                self.available_doctors.append(doctor)
        return self.available_doctors

    def get_waiting_patients_by_doctor_id(self, doctor_id: int):
        return self.doctor_repository.get_list_id_of_waiting_patients(doctor_id)

    def get_patients_sorted_by_arrival_time(self, doctor_id: int):
        waiting_list_patients_by_id = self.list_of_patients_info_by_id
        doctor_waiting_list = self.get_waiting_patients_by_doctor_id(doctor_id)
        for patient_id in doctor_waiting_list:
            waiting_list_patients_by_id.append(self.patient_repository.get_patient_by_id(patient_id))

        waiting_list_patients_by_id.sort(key=lambda date: datetime.strptime(date.patient_arrival_time, "%H:%M"))
        return waiting_list_patients_by_id

    def parse_patients(self, patients_id_list):
        parsed_list = []
        patients_id_list = patients_id_list

        for p_id in patients_id_list:
            get_info_from_id = self.patient_repository.get_patient_by_id(p_id)
            parsed_list.append(get_info_from_id)
        return parsed_list



