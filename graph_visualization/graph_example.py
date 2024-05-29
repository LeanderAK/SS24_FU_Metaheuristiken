import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import json
from graph_data import *

# use 
# pip install networkX 
# before executing this code

#def read_graph_from_file(filename:str) -> tuple[list[str],list:tuple[str,str]]:
    # Load JSON data from file
def load_graph(filename:str) -> GraphData:
    

    graph_data = GraphData()
    graph_data.fill_from_json(filename)
    return graph_data
    

def main():
    G = nx.MultiDiGraph()
     
    graph = load_graph("Data/chvatal_small.json")
    #graph = load_graph("Data/netgen_8_08a.json")
    print('start traversing')
    for node in graph.nodes:
        print(node)
        
    for edge in graph.edges:
        print(edge)
     
    #G.add_nodes_from(['A','B','C'])
    #G.add_edges_from([('A','B'),('A','C'),('C','A')])
    
    G.add_nodes_from(graph.get_nodes_as_strings())
    G.add_edges_from(graph.get_edges_as_tuples())


    pos = nx.spring_layout(G)

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
    for i, (u, v, key) in enumerate(G.edges(keys=True)):
        nx.draw_networkx_edges(G, pos, edgelist=[(u, v)], connectionstyle=f'arc3,rad={0.01 + 0.01 * i}', edge_color='gray', arrows=True, arrowstyle='-|>',arrowsize=12)

    plt.show()

if __name__ == "__main__":
    main()
    
    