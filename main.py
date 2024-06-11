import time
from solver.gurobi.gurobi_solver import GUROBISolver
from solver.output import FlowOutputer
from solver.pdm_solver import PDMSolver
from solver.settings import Settings
from solver import helper

from solver.network.network import Network
from solver.network.network_visualizer import * 

#from lib.xxSolver import XXSolver
#from lib.yySolver import YYSolver


if __name__ == '__main__':
    start_time = time.time()
    
    print('Loading settings...')
    settings = Settings()
    settings.import_settings_from_txt_file()
    print('Done \n')
    print('Start creating Network...')
    _network = Network()
    data_path = settings.get_data_path()
    dataset_name = data_path.split('/')[1]
    dataset_name = dataset_name.split('.')[0]
    _network.fill_from_json(data_path)
    print('Done \n')
    outputer = None
    flow_list = []
    print('Start solving MinCostFlow...')
    if settings.get_solver_method() ==  'PDM':
        print('Selected solover method:' + settings.get_solver_method())
        flow_list = PDMSolver.solve(_network, settings)
    elif settings.get_solver_method() == 'GUROBI':
        print('Selected solover method:' + settings.get_solver_method())
        flow_list = GUROBISolver.solve(_network)
    
        
    else:
        raise ValueError('Invalid solver method:' + settings.get_solver_method())
    print('Done')
    print('Generating output...')
    #helper.save_network_flow(network_flow)
    print('Done')
    total_time = 'Total time: ' + str(time.time() - start_time) + ' seconds'
    print(total_time)
    solver_method = settings.get_solver_method()
    outputer = FlowOutputer(
        flow_list=flow_list,
        file_path= f'Output/{solver_method}_output_{dataset_name}.txt',
        solver_method = solver_method,
        total_time = total_time)
    outputer.write_to_output_file()

