import numpy as np
import matplotlib.pyplot as plt
import networkx as nx

# Parameters for the simulation
num_vertices = 2000  # Number of vertices in the graph
degree = 8

# Create a simple undirected cycle graph
G = nx.random_regular_expander_graph(num_vertices, degree, max_tries=1000)

# Plot the graph
pos = nx.kamada_kawai_layout(G)
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=100, font_size=2)
plt.title(f"Graph with {num_vertices} vertices")
plt.show()

# Write out the graph
nx.write_gml(G, "expander_graph_2000_8.gml")
