from dal.Appointment_repository import AppointmentRepository


class AppointmentByIDListFlow:
    def __init__(self, doctor_id: int):
        self.doctor_id = doctor_id
        self.appointment_repository = AppointmentRepository()

    def get_appointment_by_doc_id(self, doctor_id: int) -> str:
        appointment = self.appointment_repository.get_appointment_by_doc_id(doctor_id)
        return appointment
