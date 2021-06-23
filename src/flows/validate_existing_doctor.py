import json

from flask import request

from dal.doctor_repository import DoctorRepository
from model.config_model import Doctor


class ValidateDoctorFlow:
    def __init__(self, doctor_id: int):
        self.doctor_id = doctor_id
        self.doctor_repository = DoctorRepository()
        self.doctor_list =  self.doctor_repository.get_all_doctors

    def check_existing_by_id(self):
        for doctor in self.doctor_list:
            if self.doctor_id == doctor.doctor_id :
                return  True
            else:
                self.create_and_append_doctor()

    def create_and_append_doctor(self):
        request_data = request.get_data()
        data = json.loads(request_data)
        doctor_id = data.get('Doctor-ID')
        doctor_name = data.get('Doctor-Name')
        doctor_phone = data.get('Doctor-Phone')
        doctor_available_status = data.get('Available-Status')
        doctor_available_dates = data.get('Available-Dates')
        doctor_specialty = data.get('Doctor-Specialty')

        doctor_obj = Doctor(doctor_id, doctor_name, doctor_phone, doctor_available_status, doctor_available_dates,
                            doctor_specialty)
        self.db.add_doctor(doctor_obj)

        print("----------------------Doctor added successfully----------------------")
        return self.db.doctors_list

