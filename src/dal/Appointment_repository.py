from dal.Inmemory_database import In_Memory_Database
from model.config_model import Appointment
import win32api


class AppointmentRepository:
    def __init__(self):
        self.db = In_Memory_Database

    def add_appointment(self, appointment: Appointment):
        self.db.add_appointment(appointment)

    def get_appointment_list(self):
        return self.db.appointments_list

    def remove_appointment(self, appointment_id: int) -> str:
        return self.db.remove_appointment(appointment_id)

    def send_notification(self) -> str:
        # alert popup window
        win32api.MessageBox(0, 'Hello, we want to inform you that the doctor is available', 'Notification!!')

