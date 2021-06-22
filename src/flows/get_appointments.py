from typing import List

from dal.appointment_repository import AppointmentRepository
from model.config_model import Appointment


class AppointmentsListFlow:
    def __init__(self):
        self.appointment_repository = AppointmentRepository()

    def get_all_appointments(self) -> List[Appointment]:
        return self.appointment_repository.get_appointment_list()




