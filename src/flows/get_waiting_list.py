from dal.Appointment_repository import AppointmentRepository


class WaitingListFlow:
    def __init__(self):
        self.appointment_repository = AppointmentRepository()

    def get_sorted_waiting_patients_list(self) -> str:
        waiting_list = self.appointment_repository.get_sorted_waiting_patients_list()
        return waiting_list
