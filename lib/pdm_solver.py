from lib.helper import get_distance_between_points


class PDMSolver:
    def __init__(self):
        print('TBD')
    
    def solve(network):
        print('TBD')
        nodes = network.get_nodes()
        supply_nodes = [key for key, value in nodes.items() if value.get('demand') < 0]
        even_nodes = [key for key, value in nodes.items() if value.get('demand') == 0]
        demand_nodes = [key for key, value in nodes.items() if value.get('demand') > 0]
        
        res = get_distance_between_points(network)
        # PDM process from the slides:
            # Nasse knoten : knoten mit überschuss
            # Ausgeglichene Knoten : knoten die gedeckt sind
            # Trockene Knoten : Bedarf nicht gedeckt
                