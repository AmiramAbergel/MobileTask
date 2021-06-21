from dataclasses import asdict

from flask import request, json
from flows.add_appointment import AddAppointmentFlow
from flows.add_to_waiting_list import AddWaitingListFlow
from flows.delete_appointment_by_id import DeleteAppointmentByIdFlow
from flows.get_appointment_by_doctor_id import AppointmentByIDListFlow
from flows.get_appointment_by_patient_id import AppointmentByPatientIDListFlow
from flows.get_appointments import AppointmentsListFlow
from flows.get_available_doctors import AvailableDoctorsListFlow
from flows.get_doctor_by_id import GetDoctorByIdFlow
from flows.get_doctors import DoctorsListFlow
from flows.get_patient_by_id import GetPatientByIdFlow
from flows.get_patients import PatientsListFlow
from flows.get_sorted_waiting_list import SortedWaitingListFlow
from flows.get_waiting_list import WaitingListFlow
from model.config_model import Appointment


def router(app):
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
        result = patient_flow.get_patient_by_id(patient_id)
        return json.dumps(result)

    @app.route('/patients/waitinglist/add/<int:patient_id>', methods=['POST'])
    def add_patient_to_waiting_list(patient_id: int) -> str:
        patient_flow = GetPatientByIdFlow(patient_id)
        patient_result = patient_flow.get_patient_by_id(patient_id)
        waiting_patient_flow = AddWaitingListFlow(patient_result)
        waiting_list_result = waiting_patient_flow.add_patient_to_waiting_list(patient_result)
        return json.dumps(waiting_list_result) # return patient that added to waiting list

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

    # Doctor Routes
    @app.route('/doctors/', methods=['GET'])
    def get_all_doctors() -> str:
        flow = DoctorsListFlow()
        result = flow.get_all_doctors()
        result_as_list_of_dict = [asdict(x) for x in result]
        return json.dumps(result_as_list_of_dict)

    @app.route('/doctors/<int:doctor_id>', methods=['GET'])
    def get_doctor_by_id(doctor_id: int) -> str:
        doctor_flow = GetDoctorByIdFlow(doctor_id)
        result = doctor_flow.get_doctor_by_id(doctor_id)
        return json.dumps(result)

    @app.route('/doctors/available', methods=['GET'])
    def get_available_doctors() -> str:
        flow = AvailableDoctorsListFlow()
        result = flow.get_available_doctors()
        result_as_list_of_dict = [asdict(x) for x in result]
        return json.dumps(result_as_list_of_dict)

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
        result = flow.remove_appointment(appointment_id)
        return {"Your appointment has been": f" {result}"}

    @app.route('/appointments/getbydocid/<int:doctor_id>', methods=['GET'])
    def get_appointment_by_doc_id(doctor_id: int) -> str:
        appointment_flow = AppointmentByIDListFlow(doctor_id)
        result = appointment_flow.get_appointment_by_doc_id(doctor_id)
        return json.dumps(result)

    @app.route('/appointments/getbypid/<int:patient_id>', methods=['GET'])
    def get_appointment_by_patient_id(patient_id: int) -> str:
        appointment_flow = AppointmentByPatientIDListFlow(patient_id)
        result = appointment_flow.get_appointment_by_patient_id(patient_id)
        return json.dumps(result)

    @app.route('/appointments/add/<int:doctor_id>', methods=['POST'])
    def add_appointment(doctor_id: int):
        # request data
        request_data = request.get_data()
        appointment_info = json.loads(request_data)
        # Appointment
        appointment_id = appointment_info.get('Appointment-ID')
        appointment_date = appointment_info.get('Appointment-Date')
        appointment_type = appointment_info.get('Type')
        # Patient
        appointment_patient_id = appointment_info.get('Patient-ID')

        # Parsed Doctor Object
        appointment_doctor_info = json.loads(get_doctor_by_id(doctor_id))
        # Parsed Patient Object
        appointment_patient_info = json.loads(get_patient_by_id(appointment_patient_id))
        # Parsed Appointment Object
        appointment = Appointment(appointment_id, appointment_date, appointment_type,
                                  doctor_id, appointment_patient_info,
                                  appointment_doctor_info)
        # flow
        appointment_flow = AddAppointmentFlow(appointment)

        if appointment_doctor_info['doctor_available_status']:         # Waiting list condition
            appointment_flow.get_notification()
            appointment_result = appointment_flow.add_appointment(appointment)
            return json.dumps(appointment_result)  # return appointment information
        else:
            res = add_patient_to_waiting_list(appointment_patient_id)
            return res


"""
        # input from user
        dae = appointment_patient_info['Patient-Name']

        schedule_appointment = input("Hello Please enter num of required appointment "f"{dae} ")
        if int(schedule_appointment) == 1:
            print
            "Its party time!!!"
        else:
            print
            "Its work time"
"""