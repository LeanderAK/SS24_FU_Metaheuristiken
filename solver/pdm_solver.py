import json
from typing import Tuple
from solver.helper import *
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

from solver.network.network import Network
from solver.network.arc import Arc
from solver.network.node import Node
from solver.path import Path


class PDMSolver:
    def __init__(self):
        print('TBD')


    def solve(network_instance: Network):

        # while not check_if_demand_fulfilled(current_network_instance):
        for i in range(10):
            #distances_at_nodes:dict[str:Tuple[float, Arc]] = do_djikstra(network_instance)      
            do_djikstra(network_instance)      
           # print(f"distances: {distances_at_nodes}")          
            demand_nodes:list[Node] = network_instance.get_demand_nodes()
            path:Path = get_path_to_closest_demand_node(demand_nodes=demand_nodes)
            max_flow:float = get_max_flow_on_path(path)

            # #add flow data
            # nodes_in_path: set = set()
            # for arc in path:
            #     nodes_in_path.add(arc.to_node)
            #     nodes_in_path.add(arc.from_node)
            #     # Can we use += here instead of accessing the value again?
            #     network_instance.flow[arc] = network_instance.flow.get(arc, 0) + max_flow
            
            # # Subtract flow from demand on all nodes in path
            # for node in nodes_in_path:
            #     node.demand = node.demand - max_flow

            # # Edit Arcs for next iteration
            # existing_arcs:list[Arc] = []
            # new_arcs:list[Arc] = []

            # for current_arc in network_instance.arcs:
            #     arc_flow = network_instance.flow.get(current_arc, 0)
            #     # E+
            #     if arc_flow < current_arc.upper_bound:
            #         print("e+", current_arc)
            #         # Yij = Yi - Yj + Cij                
            #         new_arc_cost = distances_at_nodes.get(current_arc.to_node.id)[0] - distances_at_nodes.get(current_arc.from_node.id)[0] + current_arc.cost
            #         current_arc.cost = new_arc_cost
            #         existing_arcs.append(current_arc)
            #     # E-
            #     if arc_flow > 0 and not current_arc.is_backward:
            #         print("e-", current_arc)
            #         # Yij = Yj - Yi - Cij
            #         new_arc_cost = distances_at_nodes.get(current_arc.from_node.id)[0] - distances_at_nodes.get(current_arc.to_node.id)[0] - current_arc.cost
            #         new_arc = Arc(
            #             from_node=current_arc.to_node, 
            #             to_node=current_arc.from_node, 
            #             cost= new_arc_cost,
            #             lower_bound=current_arc.lower_bound,
            #             upper_bound=current_arc.upper_bound,
            #             is_backward=True
            #         )
            #         new_arcs.append(new_arc)

            # network_instance.arcs = existing_arcs + new_arcs

            print("done iteration")

            
        # plot_network_instance(network_instance)

        
                