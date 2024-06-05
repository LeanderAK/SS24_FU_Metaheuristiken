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

from solver.network.network_visualizer import * 


class PDMSolver:
    def __init__(self):
        print('TBD')


    def solve(_network: Network):

        # while not check_if_demand_fulfilled(current_network_instance):
        for i in range(10): 
            print("range: " + str(i))
            #TODO let this go as long as requirement not fulfilled
            #distances_at_nodes:dict[str:Tuple[float, Arc]] = do_djikstra(network_instance)      
            do_djikstra(_network)      
           # print(f"distances: {distances_at_nodes}")          
            demand_nodes:list[Node] = _network.get_demand_nodes()
            path:Path = get_path_to_closest_demand_node(demand_nodes=demand_nodes)
            max_flow:float = get_max_flow_on_path(path)

            #add flow 
            for arc in path.arcs:
                arc.current_flow += max_flow
            
            # Subtract demand from target node and take it from initial node
            path.start_node.current_demand += max_flow
            path.end_node.current_demand -= max_flow

            # Hilfsnetzwerk erstellen / Edit Arcs for next iteration
            new_arcs:list[Arc] = []

            for arc in _network.arcs:
                #arc_flow = network_instance.flow.get(current_arc, 0)
                # E+
                if arc.current_flow < arc.upper_bound:
                    print("e+", arc)
                    # Yij = Yi - Yj + Cij                
                    arc.cost = arc.to_node.smallest_cost_to_arrive - arc.from_node.smallest_cost_to_arrive + arc.cost
                    new_arcs.append(arc)
                # E-
                if arc.current_flow > 0 and not arc.is_backward:
                    print("e-", arc)
                    # Yij = Yj - Yi - Cij
                    new_arc_cost = arc.from_node.smallest_cost_to_arrive - arc.to_node.smallest_cost_to_arrive - arc.cost
                    new_arc = Arc(
                        from_node=arc.to_node, 
                        to_node=arc.from_node, 
                        cost= new_arc_cost,
                        lower_bound=arc.lower_bound,
                        upper_bound=arc.upper_bound,
                        is_backward=True
                    )
                    new_arcs.append(new_arc)

            _network.arcs = new_arcs

            print("done iteration, plotting effects")
            plot_network(_network)


            
        # plot_network_instance(network_instance)

        
                