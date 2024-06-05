import json
from typing import Tuple
from lib.helper import do_djikstra
from lib.network import Arc, Network, Node
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt




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

    # TODO Infinite loop if two nodes are connected by edges in both directions
    traversal_node = shortest_distance_node
    path: list[Arc] = []
    if traversal_node is not None:
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

def check_if_demand_fulfilled(network_instance: Network) -> bool:
    demand_nodes = network_instance.get_demand_nodes()
    if len(demand_nodes) > 0:
        return False
    return True

class PDMSolver:
    def __init__(self):
        print('TBD')


    def solve(network_instance: Network):
        current_network_instance = network_instance

        # while not check_if_demand_fulfilled(current_network_instance):
        for i in range(10):
            distances = do_djikstra(current_network_instance)
            demand_nodes = current_network_instance.get_demand_nodes()
            path = get_path_to_closest_demand_node(distances= distances, demand_nodes=demand_nodes)
            max_flow = get_max_flow_on_path(path)

            # add flow data
            nodes_in_path: set = set()
            for arc in path:
                nodes_in_path.add(arc.to_node)
                nodes_in_path.add(arc.from_node)
                # Can we use += here instead of accessing the value again?
                current_network_instance.flow[arc] = current_network_instance.flow.get(arc, 0) + max_flow
            
            # Subtract flow from demand on all nodes in path
            for node in nodes_in_path:
                node.demand = node.demand - max_flow

            # Edit Arcs for next iteration
            existing_arcs:list[Arc] = []
            new_arcs:list[Arc] = []

            for current_arc in current_network_instance.arcs:
                arc_flow = current_network_instance.flow.get(current_arc, 0)
                # E+
                if arc_flow < current_arc.upper_bound:
                    print("e+", current_arc)
                    # Yij = Yi - Yj + Cij                
                    new_arc_cost = distances.get(current_arc.to_node.id)[0] - distances.get(current_arc.from_node.id)[0] + current_arc.cost
                    current_arc.cost = new_arc_cost
                    existing_arcs.append(current_arc)
                # E-
                if arc_flow > 0 and not current_arc.is_backward:
                    print("e-", current_arc)
                    # Yij = Yj - Yi - Cij
                    new_arc_cost = distances.get(current_arc.from_node.id)[0] - distances.get(current_arc.to_node.id)[0] - current_arc.cost
                    new_arc = Arc(
                        from_node=current_arc.to_node, 
                        to_node=current_arc.from_node, 
                        cost= new_arc_cost,
                        lower_bound=current_arc.lower_bound,
                        upper_bound=current_arc.upper_bound,
                        is_backward=True
                    )
                    new_arcs.append(new_arc)

            current_network_instance.arcs = existing_arcs + new_arcs

            print("done iteration")

            
        # plot_network_instance(network_instance)

        
                