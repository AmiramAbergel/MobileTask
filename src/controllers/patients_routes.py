import json
from dataclasses import asdict

from flows.get_doctors import DoctorsListFlow
from flows.get_patients import PatientsListFlow


def patient_router(app):
    # Patient Routes
    @app.route('/patients', methods=['GET'])
    def get_all_patients() -> str:
        flow = PatientsListFlow()
        result = flow.get_all_patients()
        result_as_list_of_dict = [asdict(x) for x in result]
        return json.dumps(result_as_list_of_dict)

    @app.route('/patients/<int:patient_id>', methods=['GET'])
    def get_patient_by_id(patient_id: int) -> str:
        patient_flow = PatientsListFlow()
        result = patient_flow.get_patient_by_id(patient_id)
        return json.dumps(result)

    @app.route('/patients/waiting_doctor/<int:doctor_id>', methods=['GET'])
    def get_waiting_patient_by_doc_id(doctor_id: int) -> str:
        doctor_flow = DoctorsListFlow()
        result = doctor_flow.get_waiting_patients_by_doctor_id(doctor_id)
        parsed_result = doctor_flow.parse_patients(result)
        result_as_list_of_dict = [asdict(x) for x in parsed_result]
        return json.dumps(result_as_list_of_dict)


