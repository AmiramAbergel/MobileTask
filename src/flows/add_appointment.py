from dal.Appointment_repository import AppointmentRepository
from model.config_model import Appointment


class AddAppointmentFlow:
    def __init__(self, appointment: Appointment):
        self.appointment_repository = AppointmentRepository()
        self.new_appointment = appointment

    def add_appointment(self, appointment: Appointment) -> Appointment:
        self.appointment_repository.add_appointment(appointment)
        return self.new_appointment

    def get_notification(self):
        self.appointment_repository.send_notification()
