import os
import random
import json
import yaml
import umap
import matplotlib.pyplot as plt
import numpy as np

colors = ["#b33dc6", "#e60049", "#0bb4ff", "#50e991", "#e6d800", "#9b19f5", "#ffa300", "#dc0ab4", "#b3d4ff", "#00bfa0", "#ea5545", "#f46a9b", "#ef9b20", "#edbf33", "#ede15b", "#bdcf32", "#87bc45", "#27aeef"] * 16

projection_file = 'scenarios_embeddings/paraphrase-MiniLM-L6-v2.correlation-projection.json'
meta_dir_path = 'scenarios_metadata'

group = 'Category'


embeddings = {}
with open(projection_file, 'r') as f:
    embeddings = json.load(f)


attribute_data = {}
for scenario, projection in embeddings.items():
    file_path = os.path.join(meta_dir_path, "scenario_%s.yaml" % scenario)
    attribute = 'Unknown'

    if os.path.isfile(file_path):
        with open(file_path, 'r') as stream:
            metadata = yaml.safe_load(stream)
            attribute = metadata[group]

    if attribute not in attribute_data:
        attribute_data[attribute] = []

    attribute_data[attribute].append(scenario)


fig, ax = plt.subplots()
i = 0
for attr, scenarios in attribute_data.items():
    projections = np.array(list(map(embeddings.__getitem__, scenarios)))
    x = projections[:, 0]
    y = projections[:, 1]
    ax.scatter(x, y, s=32, alpha=0.5, c=colors[i], label="%s (%d)" % (attr, len(scenarios)))

    i=i+1


ax.legend()
plt.show()
