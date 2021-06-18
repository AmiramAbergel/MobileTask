from dal.Inmemory_database import In_Memory_Database
from model.config_model import Appointment


class AppointmentRepository:
    def __init__(self):
        self.db = In_Memory_Database

    def add_appointment(self, appointment: Appointment):
        self.db.add_appointment(appointment)

    def remove_appointment(self, appointment: Appointment) -> str:
        return self.db.remove_appointment(appointment)

    def get_appointment_list(self):
        return self.db.appointment_list

    def get_sorted_waiting_patients_list(self) -> str:
        return self.db.get_waiting_patients()

    def send_notification(self) -> str:
        # send an email
        return

    def add_patient_to_waiting_list(self) -> str:
        return

