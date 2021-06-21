import json

from dal.Doctor_repository import DoctorRepository
from model.config_model import Doctor


class JsonDoctor:
    def __init__(self, doctor: Doctor):
        self.doctor_repository = DoctorRepository()
        self.doctor = doctor

    def read_and_create(self):
        doctor_data = [
            {
                "Doctor-ID": self.doctor.doctor_id,
                "Doctor-Name": self.doctor.doctor_full_name,
                "Doctor-Phone": self.doctor.doctor_phone,
                "Available-Status": self.doctor.doctor_available_status,
                "Available-Dates": self.doctor.doctor_available_dates,
                "Doctor-Specialty": self.doctor.doctor_specialty
            }
        ]

        with open('local_json/DoctorData.json', 'w') as outfile:
            json.dump(doctor_data, outfile)


