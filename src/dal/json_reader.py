import json
import logging


class JsonReader:
    @staticmethod
    def read_from_json(filepath: str):
        logging.debug("reading data from json!")
        with open(filepath, 'r') as text_file_input:
            data = text_file_input.read()
        # loading that file as a JSON object
        result_list = json.loads(data)
        return result_list
