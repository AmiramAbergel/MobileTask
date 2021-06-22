import json
from dataclasses import asdict

from flows.add_to_waiting_list import AddWaitingListFlow
from flows.get_patient_by_id import GetPatientByIdFlow
from flows.get_patients import PatientsListFlow
from flows.get_sorted_waiting_list import SortedWaitingListFlow
from flows.get_waiting_list import WaitingListFlow


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
        patient_flow = GetPatientByIdFlow(patient_id)
        result = patient_flow.get_patient_by_id()
        return json.dumps(result)

    @app.route('/patients/waitinglist/add/<int:patient_id>', methods=['POST'])
    def add_patient_to_waiting_list(patient_id: int) -> str:
        patient_flow = GetPatientByIdFlow(patient_id)
        patient_result = patient_flow.get_patient_by_id()
        waiting_patient_flow = AddWaitingListFlow(patient_result)
        waiting_list_result = waiting_patient_flow.add_patient_to_waiting_list(patient_result)
        return json.dumps(waiting_list_result)  # return patient that added to waiting list

    @app.route('/patients/waitinglist', methods=['GET'])
    def get_waiting_list() -> str:
        flow = WaitingListFlow()
        result = flow.get_waiting_list()
        result_as_list_of_dict = [asdict(x) for x in result]
        return json.dumps(result_as_list_of_dict)

    @app.route('/patients/waitinglist/sorted', methods=['GET'])
    def get_sorted_waiting_list() -> str:
        flow = SortedWaitingListFlow()
        result = flow.get_sorted_waiting_list()
        result_as_list_of_dict = [asdict(x) for x in result]
        return json.dumps(result_as_list_of_dict)