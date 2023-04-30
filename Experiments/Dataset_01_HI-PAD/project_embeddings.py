import os
import json
import yaml
import umap
import numpy as np

# Path to the directory containing the JSON files
dir_path = 'scenarios_embeddings/paraphrase-MiniLM-L6-v2'
output_filename = 'scenarios_embeddings/paraphrase-MiniLM-L6-v2.correlation-projection.json'
meta_dir_path = 'scenarios_metadata'

# List all the JSON files in the directory
file_list = os.listdir(dir_path)

# Initialize an empty array to store the embeddings
data = np.empty((len(file_list),384))
scenarios = []

# Loop through each file
for i, filename in enumerate(file_list):
    file_path = os.path.join(dir_path, filename)

    # Load the JSON file and extract the embedding array
    with open(file_path, 'r') as f:
        embedding = np.array(json.load(f), dtype=float)
        data[i] = embedding
        scenarios.append(filename.replace('scenario_', '').replace('.json', ''))


umap_embeddings = umap.UMAP(n_neighbors=20,
                            n_components=2,
                            min_dist=0.1,
                            metric='correlation').fit_transform(data)

embeddings = umap_embeddings.tolist()
projection = {scenarios[i]: embeddings[i] for i in range(len(scenarios))}

with open(output_filename, 'w') as f:
    json.dump(projection, f)