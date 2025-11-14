import networkx as nx
import matplotlib.pyplot as plt

# Instantiate a directed graph
DG = nx.DiGraph()

# Members in the research group
members = ["Gidi", "Dominic", "Kharis", "Adams", "Isaac"]

# Add nodes
DG.add_nodes_from(members)

# Add edges: everyone connected to everyone
edges = [(a, b) for a in members for b in members if a != b]
DG.add_edges_from(edges)

# customize the plot
nx.draw(DG,
        with_labels=True,
        node_color='yellow',
        edge_color='gray',
        node_size=2000,
        font_size=15,
        font_weight='bold',
        font_color='blue',
        arrows=True)

plt.show()


# 1. Number of nodes and edges
num_nodes = DG.number_of_nodes()
num_edges = DG.number_of_edges()


print("Number of Nodes:", num_nodes)
print("Number of Edges:", num_edges)


# 2. Degree distribution (in-degree + out-degree for each member)
degree_distribution = dict(DG.degree())

in_degrees = dict(DG.in_degree())

out_degrees = dict(DG.out_degree())

print("Degree Distribution:", degree_distribution)
print("In-Degree:", in_degrees)
print("Out-Degree:", out_degrees)


# 3. isolated nodes (nodes with degree 0)
isolated_nodes = list(nx.isolates(DG))

print("Isolated Nodes:", isolated_nodes)
