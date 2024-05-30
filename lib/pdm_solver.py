import json
from typing import Tuple
from lib.helper import do_djikstra
from lib.network import Arc, Network, Node


def get_path_to_closest_demand_node(distances:dict[str:Tuple[float, Arc]], demand_nodes:list[Node]) -> list[Arc]:
    shortest_distance = float('inf')
    shortest_distance_node: Node = None

    for node in demand_nodes:
        distance = distances.get(node.id)[0]
        if distance < shortest_distance:
            shortest_distance = distance
            shortest_distance_node = node

    # get Path to closest_node
    # traversal_node = Node("3", None)
    traversal_node = shortest_distance_node
    path: list[Arc] = []

    while distances.get(traversal_node.id)[1] is not None:
        arc_instance = distances.get(traversal_node.id)[1]
        path.append(arc_instance)
        traversal_node = arc_instance.from_node
    
    return path[::-1]

def get_max_flow_on_path(path: list[Arc]) -> float:
    # max_flow / lowest upper_bound
    lowest_upper_bound = float('inf')
    for arc in path:
        if arc.upper_bound < lowest_upper_bound:
            lowest_upper_bound = arc.upper_bound

    return lowest_upper_bound

class PDMSolver:
    def __init__(self):
        print('TBD')


    def solve(network_instance: Network):
        print('TBD')
        demand_nodes = network_instance.get_demand_nodes()
        # supply_nodes = network_instance.get_supply_nodes()

        distances = do_djikstra(network_instance)
        
        path = get_path_to_closest_demand_node(distances= distances, demand_nodes = demand_nodes)
        for arc in path:
            print(arc)
        max_flow = get_max_flow_on_path(path)

        # while bedarf nich auf allen bedarfsknoten gedeckt
            # do djikstra with current network
            # get_max_flow_on_path 
            # save all flows
                # dictionary : {
                #  arc : current flow on arc
                # }
            # create new network 
                # create backwards arcs
                    # edit forward arc cost
                        # Remove arc from network if upper = current_flow
            # return new_network



        # PDM process from the slides:
            # Nasse knoten : knoten mit überschuss
            # Ausgeglichene Knoten : knoten die gedeckt sind
            # Trockene Knoten : Bedarf nicht gedeckt
                