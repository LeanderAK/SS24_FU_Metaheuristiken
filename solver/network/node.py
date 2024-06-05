class Node:
    def __init__(self, id:str, demand:float):
        self.id:str = id
        self.demand:float = demand
        
    def get_name(self) -> str:
        return self.id
        
    def __str__(self):
        return self.id