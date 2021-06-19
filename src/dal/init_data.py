from dal.Inmemory_database import In_Memory_Database
from dal.json_reader import JsonReader
from flows.get_doctor_by_id import GetDoctorByIdFlow
from flows.get_patient_by_id import GetPatientByIdFlow
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
            patient_waiting_status = patient.get('Patient-Waiting-Status')

            patient_obj = Patient(patient_id, patient_name, patient_phone, patient_message, patient_waiting_status)
            self.db.add_patient(patient_obj)

        return self.db.patients_list

    def init_appointments_data(self) -> str:
        appointments_list_data = self.json_reader.read_from_json(Appointments_List_Json_File_Path)
        for appointment in appointments_list_data:
            # Appointment
            appointment_id = appointment.get('Appointment-ID')
            appointment_date = appointment.get('Appointment-Date')
            appointment_type = appointment.get('Type')
            appointment_time_slot = appointment.get('Time-Slot(Min)')
            # Patient
            appointment_patient_id = appointment.get('Patient-ID')
            # Doctor
            appointment_doctor_id = appointment.get('Doctor-ID')
            # Flow
            patient_id_flow = GetPatientByIdFlow(appointment_patient_id)
            doctor_id_flow = GetDoctorByIdFlow(appointment_doctor_id)
            # Parsed Patient Object
            filtered_patient_by_id = patient_id_flow.get_patient_by_id(appointment_patient_id)
            # Parsed Doctor Object
            filtered_doctor_by_id = doctor_id_flow.get_doctor_by_id(appointment_doctor_id)  # get doctor by id
            # Parsed Appointment Object
            appointment_obj = Appointment(appointment_id, appointment_date, appointment_type,
                                          appointment_doctor_id, filtered_patient_by_id,
                                          filtered_doctor_by_id, appointment_time_slot)
            self.db.add_appointment(appointment_obj)

        return self.db.appointments_list
