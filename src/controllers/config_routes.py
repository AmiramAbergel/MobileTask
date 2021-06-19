from dataclasses import asdict
from flask import request, json
from flows.add_appointment import AddAppointmentFlow
from flows.add_to_waiting_list import AddWaitingListFlow
from flows.delete_appointment_by_id import DeleteAppointmentByIdFlow
from flows.get_appointments import AppointmentsListFlow
from flows.get_available_doctors import AvailableDoctorsListFlow
from flows.get_doctor_by_id import GetDoctorByIdFlow
from flows.get_doctors import DoctorsListFlow
from flows.get_waiting_list import WaitingListFlow
from model.config_model import Appointment, Patient, Doctor


def router(app):
    @app.route('/patients/waiting', methods=['GET'])
    def get_all_doctors() -> str:
        flow = WaitingListFlow()
        result = flow.get_all_doctors()
        result_as_list_of_dict = [asdict(x) for x in result]
        return json.dumps(result_as_list_of_dict)

    @app.route('/doctors/', methods=['GET'])
    def get_all_doctors() -> str:
        flow = DoctorsListFlow()
        result = flow.get_all_doctors()
        result_as_list_of_dict = [asdict(x) for x in result]
        return json.dumps(result_as_list_of_dict)

    @app.route('/doctors/available', methods=['GET'])
    def get_available_doctors() -> str:
        flow = AvailableDoctorsListFlow()
        result = flow.get_available_doctors()
        result_as_list_of_dict = [asdict(x) for x in result]
        return json.dumps(result_as_list_of_dict)

    @app.route('/appointments/', methods=['GET'])
    def get_all_appointments():
        flow = AppointmentsListFlow()
        result = flow.get_all_appointments()
        result_as_list_of_dict = [asdict(x) for x in result]
        return json.dumps(result_as_list_of_dict)

    @app.route('/appointments/cancel/<int:appointment_id>', methods=['DELETE'])
    def remove_appointment(appointment_id: int) -> str:
        appointment_num = appointment_id
        flow = DeleteAppointmentByIdFlow(appointment_num)
        result = flow.remove_appointment(appointment_num)
        return {"Your appointment has been": f" {result}"}

    @app.route('/appointments/add/<int:doctor_id>', methods=['POST'])
    def add_appointment(doctor_id: int):
        # request data
        request_data = request.get_data()
        appointment_info = json.loads(request_data)

        # flow
        doctor_id_flow = GetDoctorByIdFlow(doctor_id)
        appointment_flow = AddAppointmentFlow()
        patient_flow = AddWaitingListFlow()

        # result
        filtered_doctor_by_id = doctor_id_flow.get_doctor(doctor_id)  # get doctor by id

        # Doctor
        appointment_doctor_id = doctor_id  # doctor id from user
        appointment_doctor_name = filtered_doctor_by_id.doctor_full_name  # doctor name by id from user
        appointment_doctor_phone = filtered_doctor_by_id.doctor_phone
        appointment_available_status = filtered_doctor_by_id.doctor_available_status  # doctor available status
        appointment_doctor_specialty = filtered_doctor_by_id.doctor_specialty

        # Parsed Doctor Object
        appointment_doctor_info = Doctor(appointment_doctor_id, appointment_doctor_name, appointment_doctor_phone,
                                         appointment_available_status, appointment_doctor_specialty)

        # Appointment
        appointment_id = appointment_info.get('Appointment-ID')
        appointment_date = appointment_info.get('Appointment-Date')
        appointment_type = appointment_info.get('Type')

        # Patient
        appointment_patient_id = appointment_info.get('Patient-Info')[0]["id"]
        appointment_patient_name = appointment_info.get('Patient-Info')[0]['name']
        appointment_patient_phone = appointment_info.get('Patient-Info')[0]['phone']
        appointment_patient_message = appointment_info.get('Patient-Info')[0]['message']

        # Parsed Patient Object
        appointment_patient_info = Patient(appointment_patient_id, appointment_patient_name, appointment_patient_phone,
                                           appointment_patient_message)

        # Waiting list filter

        if appointment_available_status:
            appointment_result = appointment_flow.add_appointment(appointment_id, appointment_date, appointment_type,
                                                                  appointment_doctor_id, appointment_patient_info,
                                                                  appointment_doctor_info)

            return json.dumps(appointment_result)  # return appointment information

        else:
            doctor_waiting_list_result = patient_flow.add_patient_to_waiting_list(appointment_patient_id,
                                                                                  appointment_patient_name,
                                                                                  appointment_patient_phone,
                                                                                  appointment_patient_message,
                                                                                  "waiting")

            return json.dumps(doctor_waiting_list_result)  # return patient that added to waiting list
