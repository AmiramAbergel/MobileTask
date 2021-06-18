from dal.Appointment_repository import AppointmentRepository
from model.config_model import Appointment


class AddAppointmentFlow:
    def __init__(self):
        self.appointment_data = AppointmentRepository()

    def add_appointment(self, appointment_date: str, appointment_type: str, appointment_patient_id: int,
                        appointment_doctor_id: int, appointment_doctor_name: str):
        appointment = Appointment(appointment_date, appointment_type, appointment_patient_id, appointment_doctor_id,
                                  appointment_doctor_name)
        self.appointment_data.add_appointment(appointment)
        return appointment
