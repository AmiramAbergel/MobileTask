from dal.Appointment_repository import AppointmentRepository


class DeleteAppointmentByIdFlow:
    def __init__(self, appointment_id: int):
        self.appointment_id = appointment_id
        self.appointment_repository = AppointmentRepository()

    def remove_appointment(self, appointment_id: int) -> str:
        return self.appointment_repository.remove_appointment(appointment_id)
