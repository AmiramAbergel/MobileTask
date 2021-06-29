from typing import List

from dal.inmemory_database import In_Memory_Database
from model.config_model import Appointment


class AppointmentRepository:
    def __init__(self):
        self.db = In_Memory_Database

    def add_appointment(self, appointment: Appointment):
        self.db.add_appointment(appointment)

    def get_appointment_list(self) -> List[Appointment]:
        return self.db.appointments_list

    def get_appointment_by_index(self, appointment_id: int) -> Appointment:
        return self.db.get_appointment_by_index(appointment_id)

    def get_appointments_by_patient_id(self, patient_id: int) -> List[Appointment]:
        return self.db.get_appointments_by_patient_id(patient_id)

    def get_appointments_by_doc_id(self, doctor_id: int) -> List[Appointment]:
        return self.db.get_appointments_by_doc_id(doctor_id)

    def remove_appointment(self, appointment_id: int) -> str:
        return self.db.remove_appointment(appointment_id)

    def send_notification(self) -> str:
        # alert popup window
        print( 'Hello, we want to inform you that the doctor is available', 'Notification!!')

