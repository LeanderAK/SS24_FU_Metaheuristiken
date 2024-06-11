import networkx as nx
import matplotlib.pyplot as plt
from solver.network.network import Network
import numpy as np

def plot_network(_network: Network):
    G = nx.MultiDiGraph()
     
    G.add_nodes_from(_network.get_nodes_as_strings())


    for arc in _network.arcs:
        G.add_edges_from([(arc.from_node.id, arc.to_node.id, {
            'cost': arc.cost, 
            'lower_bound': arc.lower_bound, 
            'upper_bound': arc.upper_bound, 
            'flow': arc.flow,
            'is_backward': arc.is_backward,
            'is_debug' : arc.is_debug
            })])
        
    pos = nx.circular_layout(G)

    options = {
        'node_color': 'yellow',
        'with_labels': True,
        'node_size': 700,
        'edge_color': 'gray',
        'width': 3,
        'arrowstyle': '-|>',
        'arrowsize': 12,
    }

    nx.draw_networkx_nodes(G, pos, node_size=500, node_color='skyblue')
    nx.draw_networkx_labels(G, pos)

    forward_edges = [(source_n, target_n) for source_n, target_n, edge_data in G.edges(data=True) if (edge_data.get('is_backward') != True and edge_data.get('is_debug') == False)] 
    backward_edges = [(source_n, target_n) for source_n, target_n, edge_data in G.edges(data=True) if (edge_data.get('is_backward') == True and edge_data.get('is_debug') == False)]
    debug_edges = [(source_n, target_n) for source_n, target_n, edge_data in G.edges(data=True) if edge_data.get('is_debug') == True]

    nx.draw_networkx_edges(G,pos,edgelist=forward_edges,edge_color='gray', arrows=True, arrowstyle='-|>',arrowsize=20)
    nx.draw_networkx_edges(G,pos,edgelist=backward_edges,connectionstyle=f'arc3,rad=0.3',edge_color='red', arrows=True, arrowstyle='-|>',arrowsize=20)
       
    nx.draw_networkx_edges(G,pos,edgelist=debug_edges,edge_color='blue', arrows=True, arrowstyle='-|>',arrowsize=20)

    edge_labels = {(arc.from_node.id, arc.to_node.id): f'Flow: {arc.flow} / {arc.upper_bound}, Cost: {arc.cost}' for arc in _network.arcs}

    forward_edge_labels = {(u, v): f'({u},{v})  Flow: {G[u][v][0]["flow"]} / {G[u][v][0]["upper_bound"]}, Cost: {G[u][v][0]["cost"]}' for u, v in forward_edges}
    nx.draw_networkx_edge_labels(G, pos, edge_labels=forward_edge_labels, font_color='grey')

    backward_edge_labels = {(u, v): f'({u},{v})  Flow: {G[u][v][0]["flow"]} / {G[u][v][0]["upper_bound"]}, Cost: {G[u][v][0]["cost"]}' for u, v in backward_edges}

    offset_pos =  {node: (x - 0.05, y-0.05) for node, (x, y) in pos.items()}
    nx.draw_networkx_edge_labels(G, offset_pos, edge_labels=backward_edge_labels, font_color='red')

    node_costs = {node_id: node.smallest_cost_to_arrive for node_id, node in _network.nodes.items()}
    label_pos = {node_id: (pos[node_id][0], pos[node_id][1] - 0.1) for node_id in G.nodes()}  # Adjust label positions
    for node_id, (x, y) in label_pos.items():
        nx.draw_networkx_labels(G, {node_id: (x, y)}, labels={node_id: f'{node_costs[node_id]}'}, font_size=10, font_color='black', font_weight='bold')  # Draw node labels

    node_incoming_arcs = {node_id: node.incoming_arc_with_smallest_cost.__str__() for node_id, node in _network.nodes.items()}
    label_pos = {node_id: (pos[node_id][0] - 0.1, pos[node_id][1] - 0.1) for node_id in G.nodes()}  # Adjust label positions
    for node_id, (x, y) in label_pos.items():
        nx.draw_networkx_labels(G, {node_id: (x, y)}, labels={node_id: f'{node_incoming_arcs[node_id]}'}, font_size=10, font_color='black', font_weight='300')  # Draw node labels

    node_demand = {node_id: (node.current_demand,node.initial_demand) for node_id, node in _network.nodes.items()}
    label_pos = {node_id: (pos[node_id][0] + 0.1, pos[node_id][1] - 0.1) for node_id in G.nodes()}  # Adjust label positions
    for node_id, (x, y) in label_pos.items():
        color = 'green' 
        if(node_demand[node_id][0] < 0):
            color = 'blue'
        elif(node_demand[node_id][0] > 0):
            color = 'red'
            
        nx.draw_networkx_labels(G, {node_id: (x, y)}, labels={node_id: f'{node_demand[node_id][0]} / {node_demand[node_id][1] }'}, font_size=10, font_color=color, font_weight='300')  # Draw node labels
    
    plt.show()
    

