import json
import logging
from dal.Patient_repository import PatientRepository


class JsonReader:
    def __init__(self, filepath: str):
        self.filepath = filepath
        self.patient_repository = PatientRepository()

    def read_from_json(self):
        logging.debug("reading data from json!")
        with open(self.filepath, 'r') as text_file_input:
            data = text_file_input.read()
        # loading that file as a JSON object
        result_list = json.loads(data)
        return result_list

