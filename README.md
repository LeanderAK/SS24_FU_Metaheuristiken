# Requirements:
- networkx
- matplotlib
- numpy 
- gurobipy
- pyyaml

# Setup:
- Define Solver method in Settings.yaml
<br>
```
 PDM or GUROBI
```

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

# Additional Configuration
You can also control what iterations of the network are plotted while running the PDM Algorithm. To do so you can update the ```pdm_plot_settings```in settings.yaml

# Output:
The Output is printed into txt files in the Output directory. The names are named in the following convention:
<br>
```SOLVER_METHOD_output_FILENAME.txt```