import json
from typing import Tuple
from lib.helper import *
from lib.network import Arc, Network, Node
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt


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

        
                