import json
import logging


class JsonReader:
    @staticmethod
    def read_from_json(self, filepath: str):
        logging.debug("reading data from json!")
        with open(filepath, 'r') as text_file_input:
            data = text_file_input.read()
        # loading that file as a JSON object
        list_of_messages = json.loads(data)
        return list_of_messages
