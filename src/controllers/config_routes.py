import json
from flask import request
from flows.add_appointment import AddAppointmentFlow


def router(app):

    @app.route('/doctors/', methods=['GET'])
    def get_all_doctors() -> str:
        return

    @app.route('/doctors/available', methods=['GET'])
    def get_available_doctors() -> str:
        return

    @app.route('/appointments/add', methods=['POST'])
    def add_appointment() -> str:
        request_data = request.get_data()
        data = json.loads(request_data)
        patient_id = data.get('patient-id')
        patient_full_name = data.get('patient-name')
        patient_phone = data.get('patient-phone')
        patient_message = data.get('patient-message')
        patient_arrival_time = data.get('patient-arrival-time')
        patient_waiting_status = data.get('patient-waiting-status')
        flow = AddAppointmentFlow()
        result = flow.add(patient_id, patient_full_name, patient_phone, patient_message, patient_arrival_time, patient_waiting_status)
        return result

