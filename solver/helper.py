from typing import Tuple

from solver.network.network import Network
from solver.network.arc import Arc
from solver.network.node import Node
from solver.path import Path

def save_network_flow(network_flow):
    pass

def get_node_with_shortest_distance(unexplored_nodes: list[Node]):
    shortest_distance:float = float('inf')
    closest_node: Node = None
    
    for node in unexplored_nodes:
        distance = node.smallest_cost_to_arrive
        if distance < shortest_distance:
            shortest_distance = distance
            closest_node = node

    return closest_node, shortest_distance

# adjusts the cost values on the inputted networks nodes
def do_djikstra(_network: Network): #-> dict[str:Tuple[float, Arc]]:
    # TODO manage 0 Networks
    supply_nodes = _network.get_supply_nodes()

    unexplored_nodes: list[Node] = list(_network.nodes.values())
    explored_nodes:list[Node] = [] 


    for node in unexplored_nodes:
        #cost - is the same as - distance
        node.smallest_cost_to_arrive = (0 if node in supply_nodes else float('inf'))
    
    while len(unexplored_nodes) > 0:
        node_being_explored, shortest_distance = get_node_with_shortest_distance(unexplored_nodes)
        
        explored_nodes.append(node_being_explored)
        unexplored_nodes.remove(node_being_explored)

        neighboring_nodes = _network.get_neighboring_nodes(node_being_explored)
        for neighbor_node in neighboring_nodes:
            neighbor_arc = _network.get_arc_from_to(from_node = node_being_explored, to_node = neighbor_node)

            # cost of arc + cost of current node
            new_neighbor_cost = neighbor_arc.cost + node_being_explored.smallest_cost_to_arrive

            if new_neighbor_cost < neighbor_node.smallest_cost_to_arrive:
                neighbor_node.smallest_cost_to_arrive = new_neighbor_cost
                neighbor_node.incoming_arc_with_smallest_cost = neighbor_arc


def get_path_to_closest_demand_node(demand_nodes:list[Node], supply_nodes:list[Node]) -> Path:  #TODO maybe supply nodes are not needed actually
    shortest_distance = float('inf')
    shortest_distance_node: Node = None

    print("get_path_to_closest_demand_node 1")
    for node in demand_nodes:
        distance = node.smallest_cost_to_arrive
        if distance < shortest_distance:
            shortest_distance = distance
            shortest_distance_node = node

    print("get_path_to_closest_demand_node 2")
    print(f"shortest_distance_node: {shortest_distance_node}")

    # get Path to closest_node
    # traversal_node = Node("3", None)

    # TODO Infinite loop if two nodes are connected by edges in both directions
    traversal_node = shortest_distance_node
    arc_list: list[Arc] = []
    if traversal_node is not None:
        while traversal_node.incoming_arc_with_smallest_cost is not None:
            arc = traversal_node.incoming_arc_with_smallest_cost
            arc_list.append(arc)
            traversal_node = arc.from_node
            #if(arc.from_node in supply_nodes)  # this is not redundant due to backwards arc the supply node can also have an incoming arc
            
    print("get_path_to_closest_demand_node 3")

    
    path: Path = Path(arcs = arc_list[::-1])
    
    return path

def get_max_flow_on_path(path: Path) -> float:
    # max_flow / lowest upper_bound    
    #lowest_upper_bound = float('inf')
    lowest_upper_bound =  max(0,path.end_node.current_demand)
    for arc in path.arcs:
        if arc.upper_bound < lowest_upper_bound:
            lowest_upper_bound = arc.upper_bound
            
    

    return lowest_upper_bound

def check_if_demand_fulfilled(network_instance: Network) -> bool:
    demand_nodes = network_instance.get_demand_nodes()
    if len(demand_nodes) > 0:
        return False
    return True
