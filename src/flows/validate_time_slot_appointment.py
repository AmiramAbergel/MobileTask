from dal.appointment_repository import AppointmentRepository


class ValidateTimeAppointmentFlow:
    def __init__(self, appointment_id: int, appointment_check_time: str):
        self.appointment_id = appointment_id
        self.appointment_repository = AppointmentRepository()
        self.appointment_check_time = appointment_check_time
        self.appointment_by_id = self.appointment_repository.get_appointment_by_index(self.appointment_id)

    def check_appointment_available_by_time(self):
        appointment = self.appointment_by_id
        if self.appointment_check_time != appointment.appointment_start_time:
            return True
        else:
            return False






