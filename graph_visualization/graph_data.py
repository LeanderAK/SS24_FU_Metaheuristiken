import json

class Node:
    def __init__(self, id:str, demand:float):
        self.id:str = id
        self.demand:float = demand
        
    def get_name(self) -> str:
        return self.id
        
    def __str__(self):
        return self.id

class Edge:
    def __init__(self, from_node:Node, to_node:Node, cost:float, lower_bound:float, upper_bound:float):
        self.from_node:Node = from_node
        self.to_node:Node = to_node
        self.cost:float  = cost
        self.lower_bound:float = lower_bound
        self.upper_bound:float = upper_bound
        
    def get_tuple_representation(self) -> tuple[str,str]:
        return (self.from_node,self.to_node)
    
    def __str__(self):
        return f"from: {self.from_node} to {self.to_node}"

class GraphData:
    def __init__(self):
        self.nodes:dict[Node] = {}
        self.edges:list[Edge] = []

    def fill_from_json(self, filename):
        with open(filename, "r") as file:
            json_data = json.load(file)
            for node_id, node_data in json_data["nodes"].items():
                self.nodes[node_id] = Node(node_id,node_data["demand"])
            for arc_data in json_data["arcs"]:
                self.edges.append(Edge(arc_data["from"], arc_data["to"], arc_data["cost"], arc_data["lower_bound"], arc_data["upper_bound"]))
                
    def get_nodes_as_strings(self) -> list[Node]:
        _nodes_as_strings:list[str] = []
        
        for node in self.nodes.values():  
           _nodes_as_strings.append(node.get_name())         
        
        return _nodes_as_strings
    
    def get_edges_as_tuples(self) -> list[Edge]:
        _edges_as_tuples:list[tuple[str,str]] = []
        
        for index,edge in enumerate(self.edges):  
           _edges_as_tuples.append(edge.get_tuple_representation())  
        
        return _edges_as_tuples