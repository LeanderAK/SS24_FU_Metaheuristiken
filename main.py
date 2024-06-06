import time
from solver.gurobi.gurobi_solver import GUROBISolver
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
    
    #print('Loading Inputdata...')
    #print('Done')
    print('Start creating Network...')
    _network = Network()
    _network.fill_from_json(settings.get_data_path())
    # print(_network)
    # print('Done \n')
    
    # print('Visualize Network')
    # plot_network(_network)
    print('Done \n')
    
    print('Start solving MinCostFlow...')
    if settings.get_solver_method() ==  'PDM':
        print('Selected solover method:' + settings.get_solver_method())
        network_flow = PDMSolver.solve(_network)
    elif settings.get_solver_method() == 'GUROBI':
        print('Selected solover method:' + settings.get_solver_method())
        network_flow = GUROBISolver.solve(_network)
        
    else:
        raise ValueError('Invalid solver method:' + settings.get_solver_method())
    print('Done')
    print('Generating output...')
    #helper.save_network_flow(network_flow)
    print('Done')
    print('Total time: ' + str(time.time() - start_time) + ' seconds')
    
    add_network_to_drawing(_network)

