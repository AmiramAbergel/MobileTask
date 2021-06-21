from dal.Appointment_repository import AppointmentRepository
from model.config_model import Appointment


class AppointmentByAppointmentIndexFlow:
    def __init__(self, appointment_id: int):
        self.appointment_id = appointment_id
        self.appointment_repository = AppointmentRepository()

    def get_appointment_by_index(self) -> Appointment:
        appointment = self.appointment_repository.get_appointment_by_index(self.appointment_id)
        return appointment
