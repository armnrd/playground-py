import numpy as np
import matplotlib.pyplot as plt
import networkx as nx

# Parameters for the simulation
num_vertices = 500 # Number of vertices in the graph
degree = 8
num_steps = 100000  # Total number of steps in the random walk
start_vertex = 0  # Starting vertex for the random walk

# Create a random regular expander graph
G = nx.random_regular_expander_graph(num_vertices, degree, max_tries=500)

# Initialize a dictionary to count the number of visits to each vertex
visit_counts = {i: 0 for i in range(num_vertices)}

# Start the random walk
current_vertex = start_vertex

for _ in range(num_steps):
    # Increment visit count for the current vertex
    visit_counts[current_vertex] += 1

    # Get the neighbors of the current vertex
    neighbors = list(G.neighbors(current_vertex))

    # Randomly select the next vertex from the neighbors
    current_vertex = np.random.choice(neighbors)

# Plot the graph
pos = nx.kamada_kawai_layout(G)
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=50, font_size=2)
plt.title(f"Graph with {num_vertices} vertices - Random Walk")

# Display the graph
plt.show()

# Plot the histogram of vertex visit counts
plt.bar(visit_counts.keys(), visit_counts.values(), color='blue')
plt.title(f"Histogram of Visits to Vertices after {num_steps} Steps")
plt.xlabel("Vertex")
plt.ylabel("Number of Visits")
plt.grid(True)
plt.show()
