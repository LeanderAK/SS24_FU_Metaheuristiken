import json
import os


class NetworkInput:
    loaded_data = {}

    def __init__(self):
        self.__loaded_data = {}

    def get_loaded_data(self):
        return self.__loaded_data

    def get_XYZ(self):
        return 0
    
    def load_data_from_txt_file(self, data_path_and_name):
        full_path = os.path.join(os.path.dirname(__file__), '..', data_path_and_name)

        with open(full_path, 'r') as file:
            self.__loaded_data = json.load(file)


