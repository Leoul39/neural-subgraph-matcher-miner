import pickle

edges = []

with open("C:/Users/hp/Downloads/com-youtube.ungraph.txt/com-youtube.ungraph.txt", 'r') as f:
    for line in f:
        line = line.strip()

        # Skip comment lines
        if line.startswith('#') or line == "":
            continue

        # Split by whitespace (tab or space)
        parts = line.split()

        # Convert to integers
        node1 = int(parts[0])
        node2 = int(parts[1])

        edges.append((node1, node2))

# Save as pickle
with open('c.pkl', 'wb') as f:
    pickle.dump(edges, f)

print("Saved successfully!")
