from dal.Inmemory_database import In_Memory_Database
from dal.json_reader import JsonReader
from flows.get_doctor_by_id import GetDoctorByIdFlow
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

    def init_appointments_data(self) -> str:
        appointments_list_data = self.json_reader.read_from_json(Appointments_List_Json_File_Path)

        for appointment in appointments_list_data:

            # Appointment
            appointment_id = appointment.get('Appointment-ID')
            appointment_date = appointment.get('Appointment-Date')
            appointment_type = appointment.get('Type')
            appointment_time_slot = appointment.get('Time-Slot(Min)')

            # Patient
            appointment_patient_id = appointment.get('Patient-Info')[0]["id"]
            appointment_patient_name = appointment.get('Patient-Info')[0]['name']
            appointment_patient_phone = appointment.get('Patient-Info')[0]['phone']
            appointment_patient_message = appointment.get('Patient-Info')[0]['message']

            # Doctor
            appointment_doctor_id = appointment.get('Doctor-ID')  # doctor id from user

            # Flow
            doctor_id_flow = GetDoctorByIdFlow(appointment_doctor_id)
            filtered_doctor_by_id = doctor_id_flow.get_doctor(appointment_doctor_id)  # get doctor by id

            # result
            appointment_doctor_name = filtered_doctor_by_id.doctor_full_name  # doctor name by id from user
            appointment_doctor_phone = filtered_doctor_by_id.doctor_phone
            appointment_available_status = filtered_doctor_by_id.doctor_available_status  # doctor available status
            appointment_doctor_specialty = filtered_doctor_by_id.doctor_specialty

            # Parsed Patient Object
            appointment_patient_info = Patient(appointment_patient_id, appointment_patient_name,
                                               appointment_patient_phone,
                                               appointment_patient_message)
            # Parsed Doctor Object
            appointment_doctor_info = Doctor(appointment_doctor_id, appointment_doctor_name, appointment_doctor_phone,
                                             appointment_available_status, appointment_doctor_specialty)

            # Parsed Appointment Object
            appointment_obj = Appointment(appointment_id, appointment_date, appointment_type, appointment_doctor_id, appointment_patient_info,
                                          appointment_doctor_info, appointment_time_slot)

            self.db.add_appointment(appointment_obj)

        return self.db.appointments_list
