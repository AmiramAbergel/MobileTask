from dal.appointment_repository import AppointmentRepository
from model.config_model import Appointment


class AddAppointmentFlow:
    def __init__(self):
        self.appointment_repository = AppointmentRepository()

    def add_appointment(self, appointment: Appointment) -> Appointment:
        self.appointment_repository.add_appointment(appointment)
        return appointment

    def get_notification(self):
        self.appointment_repository.send_notification()
