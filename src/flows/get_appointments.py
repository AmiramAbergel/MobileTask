from dal.Appointment_repository import AppointmentRepository


class AppointmentsListFlow:
    def __init__(self):
        self.appointment_repository = AppointmentRepository()

    def get_all_appointments(self) -> str:
        return self.appointment_repository.get_appointment_list()




