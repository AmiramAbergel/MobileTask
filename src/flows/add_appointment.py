from dal.Appointment_repository import AppointmentRepository
from model.config_model import Appointment


class AddAppointmentFlow:
    def __init__(self):
        self.appointment_repository = AppointmentRepository()

    def add_appointment(self, appointment_date: str, appointment_type: str, appointment_doctor_id: int,
                        appointment_patient_info: object, appointment_doctor_info: object):
        appointment = Appointment(appointment_date, appointment_type, appointment_doctor_id, appointment_patient_info,
                                  appointment_doctor_info)
        self.appointment_repository.add_appointment(appointment)
        return appointment
