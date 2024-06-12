from solver.network.network import Network
import gurobipy as gp
from gurobipy import Model, GRB, quicksum

from solver.output import format_flow_string

class GUROBISolver:
    def __init__(self):
        print('TBD')


    def solve(_network: Network):
        m = Model("mincostflow")
        m.setParam('OutputFlag', 0)
        flow = {}
        for arc in _network.arcs:
            flow[arc.from_node.id, arc.to_node.id] = m.addVar(lb=arc.lower_bound, ub=arc.upper_bound, obj=arc.cost, name=f'flow_{arc.from_node.id}_{arc.to_node.id}')

        for node_id, node in _network.nodes.items():
            m.addConstr(
                quicksum(flow[arc.from_node.id, arc.to_node.id] for arc in _network.arcs if arc.to_node == node) -
                quicksum(flow[arc.from_node.id, arc.to_node.id] for arc in _network.arcs if arc.from_node == node) == node.initial_demand,
                name=f'demand_{node_id}'
            )

        m.optimize()

        flow_list = []
        if m.status == GRB.OPTIMAL:
            for arc in _network.arcs:
                if flow[arc.from_node.id, arc.to_node.id].x > 0:
                    flow_list.append(format_flow_string(arc.from_node.id, arc.to_node.id, flow[arc.from_node.id, arc.to_node.id].x))
        else:
            print("No feasible solution found")
        return flow_list