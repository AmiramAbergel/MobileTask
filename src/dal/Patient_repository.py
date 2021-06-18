from dal.Appointment_repository import AppointmentRepository
from dal.Inmemory_database import In_Memory_Database
from model.config_model import Patient

Patients_List_Json_File_Path = 'local_json/Patients_list.json'


class PatientRepository:
    def __init__(self):
        self.db = In_Memory_Database
        self.appointment_data = AppointmentRepository()

    def _get_patients_data(self):
        patients_list_data = self.read_from_json(Patients_List_Json_File_Path)
        for patient in patients_list_data:
            patient_id = patient.get('Patient-ID')
            patient_name = patient.get('Patient-Name')
            patient_phone = patient.get('Patient-Phone')
            patient_message = patient.get('Patient-Message')
            patient_arrival_time = patient.get('Patient-Arrival-Time')
            patient_waiting_status = patient.get('Patient-Waiting-Status')

            patient_obj = Patient(patient_id, patient_name, patient_phone, patient_message, patient_arrival_time,
                                  patient_waiting_status)
            self.db.add_patient(patient_obj)

        return self.db.patients_list

    def get_all_doctors(self) -> str:
        return self.db.get_all_doctors()

    def get_available_doctors(self) -> str:
        return self.db.get_available_doctors()

    def add_appointment(self, patient: Patient) -> str:
        self.appointment_data.add_appointment(patient)

    def remove_appointment(self, patient: Patient) -> str:
        return self.appointment_data.remove_appointment(patient)

    def get_waiting_list(self) -> str:
        return self.appointment_data.get_sorted_waiting_patients_list()
