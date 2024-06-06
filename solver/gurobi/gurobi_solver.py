from solver.network.network import Network
import gurobipy as gp
from gurobipy import GRB

class GUROBISolver:
    def __init__(self):
        print('TBD')


    def solve(_network: Network):
        print("TBD")
        nodes = _network.nodes
        node_ids = list(nodes.keys())
        
        arcs = _network.arcs
        model = gp.Model()

        # set output level to max
        model.Params.TuneOutput = 3

        # add variable f
        f = model.addVars(node_ids, node_ids, vtype=GRB.CONTINUOUS, name='f')

        # add constraint representing supply/demand
        for node_id, node in nodes.items():
            print(node.initial_demand)
            model.addConstr(gp.quicksum(f[arc.from_node.id, arc.to_node.id] for arc in arcs) -
                            gp.quicksum(f[arc.to_node.id, arc.from_node.id] for arc in arcs)
                            == node.initial_demand)
            
            # model.addConstr(gp.quicksum(f[i,j] for (x,j) in edges if x == i) -
            #                 gp.quicksum(f[j,i] for (j,x) in edges if x == i)
            #             == supply[i])

        # add constraint on edge flows w.r.t. capacities
        for arc in arcs:
            model.addConstr(f[arc.from_node.id, arc.to_node.id] <= arc.upper_bound)

        # for (i,j) in edges:
        #     model.addConstr(f[i,j] <= capacity[i,j])

        # add constraint on edge flows w.r.t. 0
        for arc in arcs:
            model.addConstr(f[arc.from_node.id, arc.to_node.id] >= 0)

        # for (i,j) in edges:
        #     model.addConstr(f[i,j] >= 0)
            
        # set objective
        model.setObjective(gp.quicksum(arc.cost * f[arc.from_node.id, arc.to_node.id] for arc in arcs), GRB.MINIMIZE)

        # model.setObjective(gp.quicksum(cost[i,j] * f[i,j] for (i,j) in edges), GRB.MINIMIZE)

        model.optimize()
        try:
            print(f'\nObjective value found: {model.objVal}')
        except AttributeError as e:
            print(f'\nCould not find an objective value. \nTraceback:\n\t{e}')