import numpy as np
import matplotlib.pyplot as plt
import networkx as nx

# Parameters for the simulation
ground_set_size = 7  # Number of vertices in the graph
subset_size = 3
num_steps = 100  # Total number of steps in the random walk
start_vertex = 0  # Starting vertex for the random walk

# Create a Kneser graph
G = nx.kneser_graph(ground_set_size, subset_size)
num_vertices = G.number_of_nodes()

# Initialize a dictionary to count the number of visits to each vertex
visit_counts = {v: 0 for v in G}

# Start the random walk
current_vertex = list(G)[0]

for _ in range(num_steps):
    # Increment visit count for the current vertex
    visit_counts[current_vertex] += 1

    # Get the neighbors of the current vertex
    neighbors = range(len(list(G.neighbors(current_vertex))))

    # Randomly select the next vertex from the neighbors
    current_vertex = list(G.neighbors(current_vertex))[np.random.choice(neighbors)]

# Plot the graph
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=500, font_size=10)
plt.title(f"Graph with {num_vertices} vertices - Random Walk")

# Display the graph
plt.show()

# # Plot the histogram of vertex visit counts
plt.bar(range(len(visit_counts.keys())), visit_counts.values(), color='blue')
plt.title(f"Histogram of Visits to Vertices after {num_steps} Steps")
plt.xlabel("Vertex")
plt.ylabel("Number of Visits")
# plt.grid(True)
plt.show()
