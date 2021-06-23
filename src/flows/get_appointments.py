from typing import List

from dal.appointment_repository import AppointmentRepository
from model.config_model import Appointment


class AppointmentsListFlow:
    def __init__(self, identification: int):
        self.id = identification
        self.appointment_repository = AppointmentRepository()

    def get_all_appointments(self) -> List[Appointment]:
        return self.appointment_repository.get_appointment_list()

    def get_appointment_by_index(self) -> Appointment:
        appointment = self.appointment_repository.get_appointment_by_index(self.id)
        return appointment

    def get_appointment_by_doc_id(self) -> List[Appointment]:
        appointments = self.appointment_repository.get_appointments_by_doc_id(self.id)
        return appointments

    def get_appointment_by_patient_id(self) -> List[Appointment]:
        appointments = self.appointment_repository.get_appointments_by_patient_id(self.id)
        return appointments









