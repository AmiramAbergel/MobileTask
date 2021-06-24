import json
from dataclasses import asdict

from flows.get_doctors import DoctorsListFlow


def doctor_router(app):
    # Doctor Routes
    @app.route('/doctors/', methods=['GET'])
    def get_all_doctors() -> str:
        flow = DoctorsListFlow()
        result = flow.get_all_doctors()
        result_as_list_of_dict = [asdict(x) for x in result]
        return json.dumps(result_as_list_of_dict)

    @app.route('/doctors/<int:doctor_id>', methods=['GET'])
    def get_doctor_by_id(doctor_id: int) -> str:
        doctor_flow = DoctorsListFlow()
        result = doctor_flow.get_doctor_by_id(doctor_id)
        return json.dumps(result)

    @app.route('/doctors/available', methods=['GET'])
    def get_available_doctors() -> str:
        doctor_flow = DoctorsListFlow()
        result = doctor_flow.get_available_doctors()
        result_as_list_of_dict = [asdict(x) for x in result]
        return json.dumps(result_as_list_of_dict)

    @app.route('/doctor/wait_patients/<int:doctor_id>', methods=['GET'])
    def get_sorted_waiting_patients(doctor_id: int):
        doctor_flow = DoctorsListFlow()
        result = doctor_flow.get_patients_sorted_by_arrival_time(doctor_id)
        result_as_list_of_dict = [asdict(x) for x in result]
        return json.dumps(result_as_list_of_dict)

