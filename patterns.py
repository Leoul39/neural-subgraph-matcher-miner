import pickle

with open("C:/Users/hp\Downloads/decoder-plots (1)/results/patterns_all_instances.pkl", "rb") as f:
    data = pickle.load(f)

print("The type of the data: ", type(data))
print("The length of the dataset: ", len(data))
print("The keys for tha patterns: ", data.keys)
for key in data:
    print(key, len(data[key]))

# Ranking patterns by their frequency
ranked = sorted(data.items(), key=lambda x: len(x[1]), reverse=True)

for i, (pattern_id, instances) in enumerate(ranked):
    print(f"Rank {i+1}: {pattern_id}, Frequency = {len(instances)}")
