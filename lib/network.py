import json

class Node:
    def __init__(self, id:str, demand:float):
        self.id:str = id
        self.demand:float = demand
        
    def get_name(self) -> str:
        return self.id
        
    def __str__(self):
        return self.id


class Arc:
    def __init__(self, from_node:Node, to_node:Node, cost:float, lower_bound:float, upper_bound:float, is_backward: bool = False):
        self.from_node:Node = from_node
        self.to_node:Node = to_node
        self.cost:float  = cost
        self.lower_bound:float = lower_bound
        self.upper_bound:float = upper_bound
        self.is_backward:bool = is_backward
        
    def get_tuple_representation(self) -> tuple[str,str]:
        return (self.from_node,self.to_node)
    
    def __str__(self):
        return f"from: {self.from_node} to {self.to_node}"

class Network:
    def __init__(self):
        self.nodes:dict[Node] = {}
        # TODO performance bottleneck when searching for specific Arc
        self.arcs:list[Arc] = []
        self.flow: dict[Arc:float] = {}

    def fill_from_json(self, filename):
        with open(filename, "r") as file:
            json_data = json.load(file)
            for node_id, node_data in json_data["nodes"].items():
                self.nodes[node_id] = Node(node_id,node_data["demand"])

            for arc_data in json_data["arcs"]:
                from_node = self.nodes.get(arc_data["from"] )
                to_node = self.nodes.get(arc_data["to"])
                self.arcs.append(Arc(from_node, to_node, arc_data["cost"], arc_data["lower_bound"], arc_data["upper_bound"]))
                
    def get_neighboring_nodes(self, node: Node) -> list[Node]:
        neighbor_list: list[Node] = []
        for arc in self.arcs:
            if arc.from_node == node:
                 neighbor_list.append(arc.to_node)

        return neighbor_list
    
    def get_arc_from_to(self, from_node: Node, to_node: Node) -> Arc:
        # TODO performance bottleneck when searching for specific Arc
        for arc in self.arcs:
            if arc.to_node == to_node and arc.from_node == from_node:
                return arc


    def get_supply_nodes(self) -> list[Node]:
        return [node for node_id, node in self.nodes.items() if node.demand < 0]

    def get_demand_nodes(self) -> list[Node]:
        return [node for node_id, node in self.nodes.items() if node.demand > 0]

    def get_nodes_as_strings(self) -> list[Node]:
        _nodes_as_strings:list[str] = []
        
        for node in self.nodes.values():  
           _nodes_as_strings.append(node.get_name())         
        
        return _nodes_as_strings
    
    def get_edges_as_tuples(self) -> list[Arc]:
        _edges_as_tuples:list[tuple[str,str]] = []
        
        for index,edge in enumerate(self.arcs):  
           _edges_as_tuples.append(edge.get_tuple_representation())  
        
        return _edges_as_tuples