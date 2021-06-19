from dal.Appointment_repository import AppointmentRepository
from model.config_model import Appointment


class AppointmentByIDListFlow:
    def __init__(self, doctor_id: int):
        self.doctor_id = doctor_id
        self.appointment_repository = AppointmentRepository()

    def get_appointment_by_doc_id(self, doctor_id: int) -> Appointment:
        appointment = self.appointment_repository.get_appointment_by_doc_id(doctor_id)
        return appointment
