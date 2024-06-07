f = open("myfile.txt", "w")

class FlowOutputer():
    def __init__(self, flow_list, file_path, solver_method, total_time):
        self.flow_list = flow_list
        self.file_path = file_path
        self.solver_method = solver_method
        self.total_time = total_time

    def write_to_output_file(self):
        with open(self.file_path, 'w') as file:
            for string in self.flow_list:
                file.write(string + '\n')
            file.write(f'solved with:  {self.solver_method} \n')
            file.write(self.total_time)

    def __str__(self) -> str:
        return  "File Outputer"

def format_flow_string(from_node_id, to_node_id, flow):
    return f'Flow on arc {from_node_id} -> {to_node_id}: {int(flow)}'