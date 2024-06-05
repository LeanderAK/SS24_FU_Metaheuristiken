import time
from lib.pdm_solver import PDMSolver
from lib.settings import Settings
from lib.network import Network
from lib import helper
from lib.network_visualizer import * 

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
    network_instance = Network()
    network_instance.fill_from_json(settings.get_data_path())
    print(network_instance)
    print('Done \n')
    
    print('Visualize Network')
    plot_network(network_instance)
    print('Done \n')
    
    print('Start solving MinCostFlow...')
    if settings.get_solver_method() ==  'PDM':
        print('Selected solover method:' + settings.get_solver_method())
        network_flow = PDMSolver.solve(network_instance=network_instance)
    elif settings.get_solver_method() == 'YY':
        print('Selected solover method:' + settings.get_solver_method())
        #network_flow = YYSolver.solve(network)
        
    else:
        raise ValueError('Invalid solver method:' + settings.get_solver_method())
    print('Done')
    print('Generating output...')
    #helper.save_network_flow(network_flow)
    print('Done')
    print('Total time: ' + str(time.time() - start_time) + ' seconds')
