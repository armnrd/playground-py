import gurobipy as gp
from gurobipy import GRB
import numpy as np

# Problem dimensions
num_vars = 5000  # Number of decision variables
num_constraints = 2000  # Number of constraints

# Create a new Gurobi model
model = gp.Model("hard_lp")

# Generate random objective coefficients (for minimization)
np.random.seed(42)  # Set seed for reproducibility
objective_coeffs = np.random.rand(num_vars)

# Create decision variables (continuous and non-negative)
vars = model.addVars(num_vars, name="x", vtype=GRB.CONTINUOUS, lb=0)

# Set the objective function (minimization)
model.setObjective(gp.quicksum(objective_coeffs[i] * vars[i] for i in range(num_vars)), GRB.MINIMIZE)

# Generate random constraint coefficients and RHS values
A = np.random.rand(num_constraints, num_vars)  # Constraint matrix
b = np.random.rand(num_constraints) * num_vars * 0.5  # RHS values scaled to be challenging

# Add constraints to the model
for i in range(num_constraints):
    model.addConstr(gp.quicksum(A[i, j] * vars[j] for j in range(num_vars)) >= b[i], f"c_{i}")

# Optimize the model
model.optimize()

# Display results
if model.status == GRB.OPTIMAL:
    print(f"Optimal objective value: {model.objVal}")
else:
    print("No optimal solution found.")