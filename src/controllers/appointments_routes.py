from dataclasses import asdict

from flask import request, json
from flows.add_appointment import AddAppointmentFlow
from flows.delete_appointment_by_id import DeleteAppointmentByIdFlow
from flows.get_appointments import AppointmentsListFlow
from flows.get_doctors import DoctorsListFlow
from flows.get_patients import PatientsListFlow
from model.config_model import Appointment


def appointments_router(app):

    # Appointments Routes
    @app.route('/appointments', methods=['GET'])
    def get_all_appointments() -> str:
        flow = AppointmentsListFlow()
        result = flow.get_all_appointments()
        result_as_list_of_dict = [asdict(x) for x in result]
        return json.dumps(result_as_list_of_dict)

    @app.route('/appointments/cancel/<int:appointment_id>', methods=['DELETE'])
    def remove_appointment(appointment_id: int) -> dict[str, str]:
        flow = DeleteAppointmentByIdFlow(appointment_id)
        result = flow.remove_appointment()
        return {"Your appointment has been": f" {result}"}

    @app.route('/appointments/get_by_appointment_index/<int:doctor_id>', methods=['GET'])
    def get_appointment_by_appointment_index(appointment_id: int) -> str:
        appointment_flow = AppointmentsListFlow(appointment_id)
        result = appointment_flow.get_appointment_by_index()
        return json.dumps(result)

    @app.route('/appointments/get_by_doc_id/<int:doctor_id>', methods=['GET'])
    def get_appointment_by_doc_id(doctor_id: int) -> str:
        appointment_flow = AppointmentsListFlow(doctor_id)
        result = appointment_flow.get_appointment_by_doc_id()
        result_as_list_of_dict = [asdict(x) for x in result]
        return json.dumps(result_as_list_of_dict)

    @app.route('/appointments/get_by_patient_id/<int:patient_id>', methods=['GET'])
    def get_appointment_by_patient_id(patient_id: int) -> str:
        appointment_flow = AppointmentsListFlow(patient_id)
        result = appointment_flow.get_appointment_by_patient_id()
        result_as_list_of_dict = [asdict(x) for x in result]
        return json.dumps(result_as_list_of_dict)

    @app.route('/appointments/add/<int:doctor_id>', methods=['POST'])
    def add_appointment(doctor_id: int):
        # request data
        request_data = request.get_data()
        appointment_info = json.loads(request_data)
        # Appointment
        appointment_id = appointment_info.get('Appointment-ID')
        appointment_start_time = appointment_info.get('Appointment-Start')
        appointment_end_time = appointment_info.get('Appointment-End')
        appointment_type = appointment_info.get('Type')
        # Patient
        appointment_patient_id = appointment_info.get('Patient-ID')

        # Parsed Doctor Object
        appointment_doctor_info = DoctorsListFlow().get_doctor_by_id(doctor_id)
        # Parsed Patient Object
        appointment_patient_info = PatientsListFlow().get_patient_by_id(appointment_patient_id)

        # Parsed Appointment Object
        appointment = Appointment(appointment_id, appointment_start_time, appointment_end_time, appointment_type,
                                  doctor_id, appointment_patient_id ,appointment_patient_info,
                                  appointment_doctor_info)

        doctor_waiting_patients_id = appointment_doctor_info.waiting_patients_id
        # flow
        appointment_flow = AddAppointmentFlow()
        for start in appointment_doctor_info.doctor_available_start_time:
            while appointment_start_time >= start > appointment_start_time:
                appointment_doctor_info.doctor_available_status = False

        if appointment_doctor_info.doctor_available_status:         # Waiting list condition
            appointment_flow.get_notification()
            appointment_result = appointment_flow.add_appointment(appointment)
            return json.dumps(appointment_result)  # return appointment information
        else:
            doctor_waiting_patients_id.append(appointment_patient_info.patient_id)
