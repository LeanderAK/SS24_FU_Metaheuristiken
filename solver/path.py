from solver.network.arc import Arc
from solver.network.node import Node

class Path():
    def __init__(self, arcs:list[Arc]):
        self.arcs:list[Arc] = arcs
        self.nodes:list[Node] = [arcs[0].from_node]
                
        for arc in self.arcs:
            self.nodes.append(arc.to_node)                     
        
        self.start_node = self.nodes[0]
        self.end_node = self.nodes[-1]
        
    def __str__(self) -> str:
        return  '---- Path ---- \n' + '\n'.join(str(arc) + '\n' for arc in self.arcs)
        