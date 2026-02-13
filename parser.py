import networkx as nx
import pickle

input_file = "C:/Users/hp/Downloads/facebook_combined.txt/facebook_combined.txt"

# Create an undirected graph
G = nx.Graph()

# Read edge list from txt
with open(input_file, "r") as f:
    for line in f:
        if line.strip() == "":
            continue
        u, v = map(int, line.strip().split())
        G.add_edge(u, v)

# Save as .pkl
with open("facebook_friends.pkl", "wb") as f:
    pickle.dump(G, f)

print(f"Saved correctly as NetworkX graph")
print("Number of nodes:", G.number_of_nodes())
print("Number of edges:", G.number_of_edges())
