from dal.Appointment_repository import AppointmentRepository


class AppointmentsListFlow:
    def get_all_appointments(self) -> str:
        return AppointmentRepository().get_appointment_list()
