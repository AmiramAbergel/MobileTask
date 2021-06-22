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
        Name = input("Enter Doctor name       : ")
        doctor_phone = input("Enter Doctor phone    : ")
        doctor_available_status = input("Enter Doctor available status : ")
        doctor_available_times = input("Enter Doctor available times : ")
        doctor_specialty = input("Enter Doctor department : ")
        doctor_waiting_list = input("Enter Doctor waiting list : ")
        res_doctor = Doctor(self.doctor_id, Name, doctor_phone, doctor_available_status,
                            doctor_available_times, doctor_specialty, doctor_waiting_list)
        self.doctor_repository.add_doctor(res_doctor)
        print("----------------------Doctor added successfully----------------------")
