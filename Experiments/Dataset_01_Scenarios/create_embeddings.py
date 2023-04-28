from sentence_transformers import SentenceTransformer
import os
import json
import torch

model_name = 'paraphrase-MiniLM-L6-v2'
model = SentenceTransformer(model_name)

directory = 'scenarios'
output_directory = 'scenarios_embeddings'

if not os.path.exists(output_directory):
    os.makedirs(output_directory)

for filename in os.listdir(directory):
    if filename.endswith('.txt'):
        with open(os.path.join(directory, filename), 'r') as f:
            text = f.read()
        embedded = model.encode(text, convert_to_tensor=True)
        output_filename = os.path.join(output_directory, filename.replace('.txt', '.json'))
        with open(output_filename, 'w') as f:
            json.dump(embedded.tolist(), f)
