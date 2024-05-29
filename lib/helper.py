def save_network_flow(network_flow):
    pass

def get_node_with_shortest_distance(distances, finished_nodes):
    # return min(distances, key=distances.get)
    shortest_distance = float('inf')
    node_with_min_distance = None

    for node, distance in distances.items():
        if node not in finished_nodes:
            if distance < shortest_distance:
                shortest_distance = distance
                node_with_min_distance = node

    return node_with_min_distance

def get_distance_between_points(network):
    nodes = network.get_nodes()
    arcs = network.get_arcs()

    initial_route = [key for key, value in nodes.items() if value.get('demand') < 0]

    finished_nodes = [] 
    distances = {}
    for key, value in nodes.items():
        distances[key] = 0 if key in initial_route else float('inf')
    
    while not all(node in finished_nodes for node in list(nodes.keys())):
        shortest_node = get_node_with_shortest_distance(distances, finished_nodes)
        finished_nodes.append(shortest_node)
        for arc in arcs:
            if arc.get('from') == shortest_node:
                end_node = arc.get('to')
                cost = arc.get('cost')
                new_distance = distances[shortest_node] + cost

                if new_distance < distances[end_node]:
                    distances[end_node] = new_distance 
    
    return distances