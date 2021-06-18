from dataclasses import asdict
from flask import request, json
from flows.add_appointment import AddAppointmentFlow
from flows.get_doctor_by_id import GetDoctorByIdFlow
from flows.get_doctors import DoctorsListFlow
from model.config_model import Appointment


def router(app):
    @app.route('/doctors/', methods=['GET'])
    def get_all_doctors() -> str:
        flow = DoctorsListFlow()
        result = flow.get_all_doctors()
        result_as_list_of_dict = [asdict(x) for x in result]
        return json.dumps(result_as_list_of_dict)

    @app.route('/doctors/available', methods=['GET'])
    def get_available_doctors() -> str:
        flow = DoctorsListFlow()
        result = flow.get_available_doctors()
        result_as_list_of_dict = [asdict(x) for x in result]
        return json.dumps(result_as_list_of_dict)

    @app.route('/appointments/add/<int:doctor_id>', methods=['POST'])
    def add_appointment(doctor_id: int):
        doctor_id_flow = GetDoctorByIdFlow(doctor_id)
        filtered_doctor = doctor_id_flow.get_doctor(doctor_id)
        request_data = request.get_data()
        appointment_info = json.loads(request_data)
        appointment_date = appointment_info.get('Appointment-Date')
        appointment_type = appointment_info.get('Type')
        appointment_patient_id = appointment_info.get('Patient-ID')
        appointment_doctor_id = doctor_id
        appointment_doctor_name = filtered_doctor.doctor_full_name
        appointment_flow = AddAppointmentFlow()
        appointment_result = appointment_flow.add_appointment(appointment_date, appointment_type,
                                                              appointment_patient_id, appointment_doctor_id,
                                                              appointment_doctor_name)
        return json.dumps(appointment_result)