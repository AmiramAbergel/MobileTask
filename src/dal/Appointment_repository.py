from dal.Inmemory_database import In_Memory_Database
from model.config_model import Patient, Appointment


Appointments_List_Json_File_Path = 'local_json/Appointments_list.json'


class AppointmentRepository:
    def __init__(self):
        self.db = In_Memory_Database

    def _get_appointments_data(self):
        appointments_list_data = self.read_from_json(Appointments_List_Json_File_Path)

        for appointment in appointments_list_data:
            appointment_date = appointment.get('Doctor-ID')
            appointment_type = appointment.get('Doctor-Name')
            patient_id = appointment.get('Doctor-Phone')
            doctor_id = appointment.get('Available-Status')
            doctor_name = appointment.get('Doctor-Specialty')
            time_slot = appointment.get('Doctor-Specialty')

            appointment_obj = Appointment(appointment_date, appointment_type, patient_id, doctor_id, doctor_name,
                                          time_slot)
            self.db.add_appointment(appointment_obj)

        return self.db.appointments_list

    def add_appointment(self, patient: Patient) -> str:
        self.db.add(patient)

    def remove_appointment(self, patient: Patient) -> str:
        return self.db.remove_appointment(patient)

    def get_appointment_list(self):
        return self.db.appointment_list

    def get_sorted_waiting_patients_list(self) -> str:
        return self.db.get_waiting_patients()

    def send_notification(self) -> str:
        # send an email
        return

    def add_patient_to_waiting_list(self) -> str:
        return

