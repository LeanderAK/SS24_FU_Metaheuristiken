#To access a file from lib within lib:
#from lib.arc import Arc

class Network:
    def __init__(self, network_input):
        # print('TBD')
        # get_loaded_data returns the json data specified in the file in the settings.txt as a dict.
        # Here We need to format the data to be ready for our solver I think.
        # The solver logic will be in pdm_solver.py
        print(network_input.get_loaded_data)