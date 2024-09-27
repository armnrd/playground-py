import gurobipy as gp
from gurobipy import GRB

# Create a new model
model = gp.Model("example_lp")
# Create variables
x = model.addVar(name="x", vtype=GRB.CONTINUOUS, lb=0)
y = model.addVar(name="y", vtype=GRB.CONTINUOUS, lb=0)

# Set objective function: maximize 3x + 2y
model.setObjective(3 * x + 2 * y, GRB.MAXIMIZE)

# Add constraints
model.addConstr(x + y <= 4, "c0")
model.addConstr(x <= 2, "c1")
model.addConstr(y <= 3, "c2")

# Optimize the model
model.optimize()

# Display the results
if model.status == GRB.OPTIMAL:
    print(f"Optimal objective value: {model.objVal}")
    for v in model.getVars():
        print(f"{v.varName}: {v.x}")
else:
    print("No optimal solution found.")
