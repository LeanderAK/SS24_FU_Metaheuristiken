class Node:
    def __init__(self, id:str, initial_demand:float):
        self.id:str = id
        self.initial_demand:float = initial_demand
        self.current_demand:float = self.initial_demand
        self.smallest_cost_to_arrive:float = float('inf')
        self.incoming_arc_with_smallest_cost = None
        
    def get_name(self) -> str:
        return self.id
        
    def __str__(self):
        return self.id