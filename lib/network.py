#To access a file from lib within lib:
#from lib.arc import Arc

class Network:
    nodes = {}
    arcs = []

    def __init__(self):
        self.__nodes = {}
        self.__arcs = []

    def get_nodes(self):
        return self.__nodes

    def get_arcs(self):
        return self.__arcs
    
    def __init__(self, network_input):
        # print('TBD')
        # get_loaded_data returns the json data specified in the file in the settings.txt as a dict.
        # Here We need to format the data to be ready for our solver I think.
        # The solver logic will be in pdm_solver.py

        loaded_data = network_input.get_loaded_data()
        self.__nodes = loaded_data.get('nodes')
        self.__arcs = loaded_data.get('arcs')
        
      

