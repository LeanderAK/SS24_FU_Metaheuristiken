from solver.network.network import Network
import gurobipy as gp
from gurobipy import Model, GRB, quicksum

class GUROBISolver:
    def __init__(self):
        print('TBD')


    def solve(_network: Network):
        print("TBD")
        nodes = {
            "1": {"demand": -9},
            "2": {"demand": 4},
            "3": {"demand": 17},
            "4": {"demand": 1},
            "5": {"demand": -5},
            "6": {"demand": -8}
        }

        arcs = [
            {"from": "1", "to": "2", "cost": 3, "lower_bound": 0, "upper_bound": 2},
            {"from": "1", "to": "3", "cost": 5, "lower_bound": 0, "upper_bound": 10},
            {"from": "1", "to": "5", "cost": 1, "lower_bound": 0, "upper_bound": 10},
            {"from": "2", "to": "3", "cost": 1, "lower_bound": 0, "upper_bound": 6},
            {"from": "4", "to": "2", "cost": 4, "lower_bound": 0, "upper_bound": 8},
            {"from": "4", "to": "3", "cost": 1, "lower_bound": 0, "upper_bound": 9},
            {"from": "5", "to": "3", "cost": 6, "lower_bound": 0, "upper_bound": 9},
            {"from": "5", "to": "4", "cost": 1, "lower_bound": 0, "upper_bound": 10},
            {"from": "5", "to": "6", "cost": 1, "lower_bound": 0, "upper_bound": 6},
            {"from": "6", "to": "2", "cost": 1, "lower_bound": 0, "upper_bound": 7},
            {"from": "6", "to": "4", "cost": 1, "lower_bound": 0, "upper_bound": 8},
        ]

        # Create a new model
        m = Model("mincostflow")

        # Create variables
        flow = {}
        for arc in arcs:
            flow[arc["from"], arc["to"]] = m.addVar(lb=arc["lower_bound"], ub=arc["upper_bound"], obj=arc["cost"], name=f'flow_{arc["from"]}_{arc["to"]}')

        # Add demand constraints
        for node in nodes:
            m.addConstr(
                quicksum(flow[arc["from"], arc["to"]] for arc in arcs if arc["to"] == node) -
                quicksum(flow[arc["from"], arc["to"]] for arc in arcs if arc["from"] == node) == nodes[node]["demand"],
                name=f'demand_{node}'
            )

        # Optimize the model
        m.optimize()

        # Print the results
        if m.status == GRB.OPTIMAL:
            print("Optimal solution found:")
            for arc in arcs:
                print(f'Flow on arc {arc["from"]} -> {arc["to"]}: {flow[arc["from"], arc["to"]].x}')
        else:
            print("No feasible solution found")