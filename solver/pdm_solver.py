import json
from typing import Tuple
from solver.helper import *
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

from solver.network.network import Network
from solver.network.arc import Arc
from solver.network.node import Node
from solver.output import format_flow_string
from solver.path import Path

from solver.network.network_visualizer import * 


class PDMSolver:
    def __init__(self):
        print('TBD')


    def solve(_network: Network):

        # for i in range(10): 
        while not check_if_demand_fulfilled(_network):
            # print("range: " + str(i))
            #TODO let this go as long as requirement not fulfilled
            #distances_at_nodes:dict[str:Tuple[float, Arc]] = do_djikstra(network_instance)      
            do_djikstra(_network)   
            # plot_network(_network)
           # print(f"distances: {distances_at_nodes}") 
            demand_nodes:list[Node] = _network.get_demand_nodes()
            supply_nodes:list[Node] = _network.get_supply_nodes()
            path:Path = get_path_to_closest_demand_node(demand_nodes=demand_nodes, supply_nodes=supply_nodes)
            # print(f"path:  {path}")  
            max_flow:float = get_max_flow_on_path(path)
            # print(f"max_flow {max_flow}")  
            #add flow 
            for arc in path.arcs:
                arc.flow += max_flow
            

            # Subtract demand from target node and take it from initial node
            path.start_node.current_demand += max_flow
            path.end_node.current_demand -= max_flow


            # Hilfsnetzwerk erstellen / Edit Arcs for next iteration
            arcs:list[Arc] = list(_network.arcs)
            new_arcs:list[Arc] = []
            for arc in arcs:
                #arc_flow = network_instance.flow.get(current_arc, 0)
                # E+
                # if arc.flow < arc.upper_bound and arc.is_backward == False:
                if arc.is_backward == False:
                    # print("create forward ", arc)
                    # Yij = Yi - Yj + Cij                
                    new_arc_cost = arc.from_node.smallest_cost_to_arrive - arc.to_node.smallest_cost_to_arrive + arc.cost
                    new_arc = Arc(
                        from_node=arc.from_node, 
                        to_node=arc.to_node, 
                        cost= new_arc_cost,
                        lower_bound=arc.lower_bound,
                        upper_bound=arc.upper_bound,
                        flow= arc.flow,
                        is_backward=False
                    )
                    new_arcs.append(new_arc)

                # E-
                if arc.flow > 0 and arc.is_backward == False:
                    # print("create backword ", arc)
                    # Yij = Yj - Yi - Cij
                    # print(f"new_arc_cost = arc.to_node.smallest_cost_to_arrive - arc.from_node.smallest_cost_to_arrive - arc.cost")
                    # print(f"new_arc_cost = {arc.to_node.smallest_cost_to_arrive} - {arc.from_node.smallest_cost_to_arrive} - {arc.cost}")
                    # print(f"new_arc_cost = arc.to_node - arc.from_node")
                    # print(f"new_arc_cost = {arc.to_node} - {arc.from_node}")
                    new_arc_cost = arc.to_node.smallest_cost_to_arrive - arc.from_node.smallest_cost_to_arrive - arc.cost
                    # print(f"new_arc_cost: = {new_arc_cost}")

                    # Does backward arc exist? If so update!
                    new_arc = Arc(
                        from_node=arc.to_node, 
                        to_node=arc.from_node, 
                        cost= new_arc_cost,
                        lower_bound=arc.lower_bound,
                        upper_bound=arc.flow,
                        flow = 0,
                        is_backward=True
                    )
                    new_arcs.append(new_arc)

            # print('solve 4')
            _network.arcs = new_arcs

            # print("done iteration, plotting effects")
            # plot_network(_network)

        flow_list = []
        for arc in _network.arcs:
            if arc.flow > 0:
                flow_list.append(format_flow_string(arc.from_node.id, arc.to_node.id, arc.flow))
        return flow_list
        # plot_network_instance(network_instance)

        
                