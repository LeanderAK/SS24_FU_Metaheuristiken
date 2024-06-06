from solver.network.network import Network
import gurobipy as gp
from gurobipy import Model, GRB, quicksum

class GUROBISolver:
    def __init__(self):
        print('TBD')


    def solve(_network: Network):
        # Create a new model
        m = Model("mincostflow")

        # Create variables
        flow = {}
        for arc in _network.arcs:
            flow[arc.from_node.id, arc.to_node.id] = m.addVar(lb=arc.lower_bound, ub=arc.upper_bound, obj=arc.cost, name=f'flow_{arc.from_node.id}_{arc.to_node.id}')

        # Add demand constraints
        for node_id, node in _network.nodes.items():
            m.addConstr(
                quicksum(flow[arc.from_node.id, arc.to_node.id] for arc in _network.arcs if arc.to_node == node) -
                quicksum(flow[arc.from_node.id, arc.to_node.id] for arc in _network.arcs if arc.from_node == node) == node.initial_demand,
                name=f'demand_{node_id}'
            )

        # Optimize the model
        m.optimize()

        # Print the results
        if m.status == GRB.OPTIMAL:
            print("Optimal solution found:")
            for arc in _network.arcs:
                print(f'Flow on arc {arc.from_node.id} -> {arc.to_node.id}: {flow[arc.from_node.id, arc.to_node.id].x}')
        else:
            print("No feasible solution found")