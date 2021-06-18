from dal.Inmemory_database import In_Memory_Database
from dal.json_reader import JsonReader
from model.config_model import Doctor, Patient, Appointment

Appointments_List_Json_File_Path = 'local_json/Appointments_list.json'
Doctors_List_Json_File_Path = 'local_json/Doctors_list.json'
Patients_List_Json_File_Path = 'local_json/Patients_list.json'


class InitData:
    def __init__(self):
        self.json_reader = JsonReader()
        self.db = In_Memory_Database

    def init_doctors_data(self) -> str:
        doctors_list_data = self.json_reader.read_from_json(Doctors_List_Json_File_Path)
        for doctor in doctors_list_data:
            doctor_id = doctor.get('Doctor-ID')
            doctor_name = doctor.get('Doctor-Name')
            doctor_phone = doctor.get('Doctor-Phone')
            doctor_available_status = doctor.get('Available-Status')
            patient_specialty = doctor.get('Doctor-Specialty')

            doctor_obj = Doctor(doctor_id, doctor_name, doctor_phone, doctor_available_status, patient_specialty)
            self.db.add_doctor(doctor_obj)

        return self.db.doctors_list

    def init_patients_data(self) -> str:
        patients_list_data = self.json_reader.read_from_json(Patients_List_Json_File_Path)
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

    def _init_appointments_data(self) -> str:
        appointments_list_data = self.json_reader.read_from_json(Appointments_List_Json_File_Path)

        for appointment in appointments_list_data:
            appointment_date = appointment.get('Appointment-Date')
            appointment_type = appointment.get('Type')
            appointment_patient_id = appointment.get('Patient-ID')
            appointment_doctor_id = appointment.get('Doctor-ID')
            appointment_doctor_name = appointment.get('Doctor-Name')
            appointment_time_slot = appointment.get('Time-Slot(Min)')

            appointment_obj = Appointment(appointment_date, appointment_type, appointment_patient_id, appointment_doctor_id, appointment_doctor_name,
                                          appointment_time_slot)
            self.db.add_appointment(appointment_obj)

        return self.db.appointments_list
