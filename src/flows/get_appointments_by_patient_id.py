from typing import List
from dal.Appointment_repository import AppointmentRepository
from model.config_model import Appointment


class AppointmentsByPatientIDListFlow:
    def __init__(self, patient_id: int):
        self.patient_id = patient_id
        self.appointment_repository = AppointmentRepository()

    def get_appointment_by_patient_id(self) -> List[Appointment]:
        appointments = self.appointment_repository.get_appointments_by_patient_id(self.patient_id)
        return appointments
