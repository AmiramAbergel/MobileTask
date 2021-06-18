from dal.Appointment_repository import AppointmentRepository
from dal.Inmemory_database import In_Memory_Database
from model.config_model import Doctor

Doctors_List_Json_File_Path = 'local_json/Doctors_list.json'


class DoctorRepository:
    def __init__(self):
        self.db = In_Memory_Database
        self.appointment_data = AppointmentRepository()

    def _get_doctors_data(self):
        doctors_list_data = self.read_from_json(Doctors_List_Json_File_Path)
        for doctor in doctors_list_data:
            doctor_id = doctor.get('Doctor-ID')
            doctor_name = doctor.get('Doctor-Name')
            doctor_phone = doctor.get('Doctor-Phone')
            doctor_available_status = doctor.get('Available-Status')
            patient_specialty = doctor.get('Doctor-Specialty')

            doctor_obj = Doctor(doctor_id, doctor_name, doctor_phone, doctor_available_status, patient_specialty)
            self.db.add_doctor(doctor_obj)

        return self.db.doctors_list

    def get_sorted_waiting_patients_list(self) -> str:
        return self.appointment_data.get_sorted_waiting_patients_list()
