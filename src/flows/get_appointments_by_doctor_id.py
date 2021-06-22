from typing import List
from dal.appointment_repository import AppointmentRepository
from model.config_model import Appointment


class AppointmentsByDoctorIDListFlow:
    def __init__(self, doctor_id: int):
        self.doctor_id = doctor_id
        self.appointment_repository = AppointmentRepository()

    def get_appointment_by_doc_id(self) -> List[Appointment]:
        appointments = self.appointment_repository.get_appointments_by_doc_id(self.doctor_id)
        return appointments
