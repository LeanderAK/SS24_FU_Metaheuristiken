# Requirements:
- networkx
- matplotlib
- numpy 
- gurobipy

# Setup:
- Define Solver method in Settings.txt
<br>
```'PDM' or 'GUROBI'```

- Define filepath for input data. This should be a JSON file with the following layout:
```
{
  "nodes": {
    ID: {"demand": C}, ...
  },
  "arcs": [
    {
      "from": ID,
      "to": ID,
      "cost": X,
      "lower_bound": X,
      "upper_bound": X
    }, ...
  ]
}

```
- run Main.py

# Output:
The Output is printed into txt files in the Output directory. The names are named in fhte following convention:
<br>
```SOLVER_METHOD_output_FILENAME.txt```