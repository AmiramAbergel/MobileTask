from dal.Appointment_repository import AppointmentRepository


class AppointmentByPatientIDListFlow:
    def __init__(self, patient_id: int):
        self.patient_id = patient_id
        self.appointment_repository = AppointmentRepository()

    def get_appointment_by_patient_id(self, patient_id: int) -> str:
        appointment = self.appointment_repository.get_appointment_by_patient_id(patient_id)
        return appointment
