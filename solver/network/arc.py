from solver.network.node import Node

class Arc:
    def __init__(self, from_node:Node, to_node:Node, cost:float, lower_bound:float, upper_bound:float, flow:float = 0, is_backward: bool = False, is_debug = False):
        self.from_node:Node = from_node
        self.to_node:Node = to_node
        
        self.cost:float  = cost
        self.lower_bound:float = lower_bound
        self.upper_bound:float = upper_bound
        
        self.flow = flow
        
        self.is_backward:bool = is_backward
        self.is_debug = is_debug
        
    def get_tuple_string_representation(self) -> tuple[str,str]:
        return (self.from_node.id,self.to_node.id)
    
    def __str__(self):
        backwards_string:str = ''
        if(self.is_backward):
            backwards_string = '-is_backwards'
        
        return f"from: {self.from_node} to {self.to_node}"
    
    def get_remaining_flow(self) -> float:
        return self.upper_bound - self.flow
    
    def has_filled_capacity(self) -> bool:
        return self.flow == self.upper_bound
