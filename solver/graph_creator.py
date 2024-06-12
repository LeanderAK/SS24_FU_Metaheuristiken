# import json
# import random

# network = {
#     "nodes": {
#         "S": {"demand": -100},
#         "T": {"demand": 100}
#     },
#     "arcs": []
# }

# # Adding nodes
# for i in range(1, 101):
#     network["nodes"][str(i)] = {"demand": 0}

# # Connecting source to nodes 1-100
# for i in range(1, 11):
#     network["arcs"].append({"from": "S", "to": str(i), "cost": 1, "lower_bound": 0, "upper_bound": 10})

# # Connecting nodes 901-1000 to target 
# for i in range(91, 101):
#     network["arcs"].append({"from": str(i), "to": "T", "cost": 1, "lower_bound": 0, "upper_bound": 10})

# # Connecting each node to every other node
# for i in range(1, 101):
#     for j in range(i + 1, 101):
#         network["arcs"].append({"from": str(i), "to": str(j), "cost": 0, "lower_bound": 0, "upper_bound": 2})
#         #network["arcs"].append({"from": str(i), "to": str(j), "cost": 0, "lower_bound": 0, "upper_bound": 10})
#         #network["arcs"].append({"from": str(i), "to": str(j), "cost": 0, "lower_bound": 0, "upper_bound": random.randint(1, 10)})

# # Convert to JSON
# network_json = json.dumps(network, indent=4)

# # Save to a file
# with open('mega_network_up_2.json', 'w') as f:
#     f.write(network_json)
    

import json
import random

network = {
    "nodes": {
        "S": {"demand": -100},
        "T": {"demand": 100}
    },
    "arcs": []
}

# Adding nodes
for i in range(1, 101):
    network["nodes"][str(i)] = {"demand": 0}

# Connecting source to nodes 1-100
for i in range(1, 11):
    network["arcs"].append({"from": "S", "to": str(i), "cost": 1, "lower_bound": 0, "upper_bound": 10})

# Connecting nodes 901-1000 to target 
for i in range(91, 101):
    network["arcs"].append({"from": str(i), "to": "T", "cost": 1, "lower_bound": 0, "upper_bound": 10})

# Connecting each node to every other node
for i in range(1, 101):
    for j in range(1, 101):
        if i != j:
            #network["arcs"].append({"from": str(i), "to": str(j), "cost": 0, "lower_bound": 0, "upper_bound": 2})
            network["arcs"].append({"from": str(i), "to": str(j), "cost": 0, "lower_bound": 0, "upper_bound": 30})
            #network["arcs"].append({"from": str(i), "to": str(j), "cost": 0, "lower_bound": 0, "upper_bound": 10})
            #network["arcs"].append({"from": str(i), "to": str(j), "cost": 0, "lower_bound": 0, "upper_bound": random.randint(1, 10)})

# Convert to JSON
network_json = json.dumps(network, indent=4)

# Save to a file
with open('mega_network_up_1_to_10.json', 'w') as f:
    f.write(network_json)
    