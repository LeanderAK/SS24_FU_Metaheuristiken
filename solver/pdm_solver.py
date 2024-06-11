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
from solver.settings import Settings 


class PDMSolver:
    def __init__(self):
        print('TBD')


    def solve(_network: Network, settings: Settings = None):
        while not check_if_demand_fulfilled(_network): 
            plot_settings = settings.get_pdm_plot_settings()

            do_djikstra(_network)   

            if plot_settings['plot_djikstra'] == True:
                plot_network(_network)
            demand_nodes:list[Node] = _network.get_demand_nodes()
            supply_nodes:list[Node] = _network.get_supply_nodes()
            path:Path = get_path_to_closest_demand_node(demand_nodes=demand_nodes, supply_nodes=supply_nodes)
            max_flow:float = get_max_flow_on_path(path)
            for arc in path.arcs:
                arc.flow += max_flow
            
            path.start_node.current_demand += max_flow
            path.end_node.current_demand -= max_flow

            arcs:list[Arc] = list(_network.arcs)
            new_arcs:list[Arc] = []
            for arc in arcs:
                if arc.is_backward == False:             
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
                    new_arc_cost = arc.to_node.smallest_cost_to_arrive - arc.from_node.smallest_cost_to_arrive - arc.cost

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

            _network.arcs = new_arcs

            if plot_settings['plot_pdm'] == True:
                plot_network(_network)

        flow_list = []
        for arc in _network.arcs:
            if arc.flow > 0:
                flow_list.append(format_flow_string(arc.from_node.id, arc.to_node.id, arc.flow))

        if plot_settings['plot_final'] == True:
            plot_network(_network)
        return flow_list

        
                