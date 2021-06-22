import logging
from controllers.appointments_routes import appointments_router
from controllers.config_index_route import index_router
from controllers.doctors_routes import doctor_router
from controllers.patients_routes import patient_router
from dal.write_data import WriteData

Appointments_List_Json_File_Path = 'local_json/Appointments_list.json'
Doctors_List_Json_File_Path = 'local_json/Doctors_list.json'
Patients_List_Json_File_Path = 'local_json/Patients_list.json'


def create_app():
    logger = logging.getLogger("gunicorn.error")
    try:
        logger.info("starting create_app")
        from flask import Flask
        # Create app
        app = Flask(__name__)
        """
        Routes
        """
        index_router(app)
        appointments_router(app)
        patient_router(app)
        doctor_router(app)
        """
        Initialize DB
        """
        WriteData(Patients_List_Json_File_Path).init_patients_data()
        WriteData(Doctors_List_Json_File_Path).init_doctors_data()
        WriteData(Appointments_List_Json_File_Path).init_appointments_data()

        return app
    except Exception:
        logger.exception(f"Error starting flask App")
        raise
