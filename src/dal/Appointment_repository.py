from dal.Inmemory_database import In_Memory_Database


class AppointmentRepository:
    def __init__(self):
        self.db = In_Memory_Database

    def get_appointment_list(self):
        return self.db.appointment_list

    def get_sorted_waiting_patients_list(self) -> str:
        return self.db.get_waiting_patients()

    def send_notification(self) -> str:
        # send an email
        return

    def add_patient_to_waiting_list(self) -> str:
        return

