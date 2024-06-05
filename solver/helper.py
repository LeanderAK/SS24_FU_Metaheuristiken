from typing import Tuple

from solver.network.network import Network
from solver.network.arc import Arc
from solver.network.node import Node

def save_network_flow(network_flow):
    pass

def get_node_with_shortest_distance(distances, unexplored_nodes):
    shortest_distance = float('inf')
    closest_node: Node = None
    for node in unexplored_nodes:
        distance = distances.get(node.id)[0]
        if distance < shortest_distance:
            shortest_distance = distance
            closest_node = node

    return closest_node, shortest_distance

def do_djikstra(_network: Network) -> dict[str:Tuple[float, Arc]]:
    # TODO manage 0 Networks
    supply_nodes = _network.get_supply_nodes()

    unexplored_nodes: list[Node] = list(_network.nodes.values())
    finished_nodes:list[Node] = [] 

    # {
    #     node_id : (node_cost, incoming arc to node)
    # }
    distances:dict[str:Tuple[float, Arc]] = {}

    for node in unexplored_nodes:
        distances[node.id] = (0 if node in supply_nodes else float('inf'), None)
    
    # while not all(node in finished_nodes for node in _network.arcs):
    for i in range(6):
        closest_node, shortest_distance = get_node_with_shortest_distance(distances, unexplored_nodes)
        if closest_node is not None:
            finished_nodes.append(closest_node)
            unexplored_nodes.remove(closest_node)

            neighboring_nodes = _network.get_neighboring_nodes(closest_node)
            for neighbor_node in neighboring_nodes:
                neighbor_arc = _network.get_arc_from_to(from_node = closest_node, to_node = neighbor_node)

                closest_node_cost = distances.get(closest_node.id)[0]
                # cost of arc + cost of current node
                new_neighbor_cost = neighbor_arc.cost + closest_node_cost
                current_neighbor_cost = distances.get(neighbor_node.id)[0]

                if new_neighbor_cost < current_neighbor_cost:
                    current_neighbor_cost = new_neighbor_cost
                    distances[neighbor_node.id] = (current_neighbor_cost, neighbor_arc)

    return distances

def get_path_to_closest_demand_node(distances:dict[str:Tuple[float, Arc]], demand_nodes:list[Node]) -> list[Arc]:
    shortest_distance = float('inf')
    shortest_distance_node: Node = None

    for node in demand_nodes:
        distance = distances.get(node.id)[0]
        if distance < shortest_distance:
            shortest_distance = distance
            shortest_distance_node = node

    # get Path to closest_node
    # traversal_node = Node("3", None)

    # TODO Infinite loop if two nodes are connected by edges in both directions
    traversal_node = shortest_distance_node
    path: list[Arc] = []
    if traversal_node is not None:
        while distances.get(traversal_node.id)[1] is not None:
            arc_instance = distances.get(traversal_node.id)[1]
            path.append(arc_instance)
            traversal_node = arc_instance.from_node
    
    return path[::-1]

def get_max_flow_on_path(path: list[Arc]) -> float:
    # max_flow / lowest upper_bound
    lowest_upper_bound = float('inf')
    for arc in path:
        if arc.upper_bound < lowest_upper_bound:
            lowest_upper_bound = arc.upper_bound

    return lowest_upper_bound

def check_if_demand_fulfilled(network_instance: Network) -> bool:
    demand_nodes = network_instance.get_demand_nodes()
    if len(demand_nodes) > 0:
        return False
    return True
