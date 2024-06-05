import networkx as nx
import matplotlib.pyplot as plt
from lib.network.network import Network

###
# Helper file used for visualizing the graph
###

# use 
# pip install networkX 
# before executing this code
    
def plot_network(_network: Network):
    G = nx.MultiDiGraph()
     
    #cost etc needs to be added here
    G.add_nodes_from(_network.get_nodes_as_strings())


    for arc in _network.arcs:
        G.add_edges_from([(arc.from_node.id, arc.to_node.id, {
            'cost': arc.cost, 
            'lower_bound': arc.lower_bound, 
            'upper_bound': arc.upper_bound, 
            'is_backward': arc.is_backward
            })])
        
    
    #pos = nx.spring_layout(G)
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


    # Draw nodes
    nx.draw_networkx_nodes(G, pos, node_size=500, node_color='skyblue')

    # Draw labels
    nx.draw_networkx_labels(G, pos)


    # Draw edges
    forward_edges = [(source_n, target_n) for source_n, target_n, edge_data in G.edges(data=True) if edge_data.get('is_backward') != True]
    backward_edges = [(source_n, target_n) for source_n, target_n, edge_data in G.edges(data=True) if edge_data.get('is_backward') == True]
    
   
    #for i in enumerate(forward_edges):
    nx.draw_networkx_edges(G,pos,forward_edges,edge_color='gray', arrows=True, arrowstyle='-|>',arrowsize=20)
    nx.draw_networkx_edges(G,pos,backward_edges,connectionstyle=f'arc3,rad=0.3',edge_color='red', arrows=True, arrowstyle='-|>',arrowsize=20)
    
    #for i, (source_n, target_n, key) in enumerate(G.edges(keys=True)):
    #    nx.draw_networkx_edges(G, pos, edgelist=[(source_n, target_n)], connectionstyle=f'arc3,rad={0.01 + 0.01 * i}', edge_color='gray', arrows=True, arrowstyle='-|>',arrowsize=12)

    plt.show()
    

