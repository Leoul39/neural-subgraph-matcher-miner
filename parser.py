import networkx as nx
import pickle

G = nx.Graph()  # undirected graph

with open("C:/Users/hp/Downloads/com-youtube.ungraph.txt/com-youtube.ungraph.txt", "r") as f:
    for line in f:
        # Skip comments or empty lines
        if line.startswith("#") or line.strip() == "":
            continue
        
        u, v = map(int, line.strip().split())
        G.add_edge(u, v)

with open("youtube_ungraph_pro.pkl", "wb") as f:
    pickle.dump(G, f)

print("Saved correctly as NetworkX graph")
print("Number of nodes:", G.number_of_nodes())
print("Number of edges:", G.number_of_edges())
