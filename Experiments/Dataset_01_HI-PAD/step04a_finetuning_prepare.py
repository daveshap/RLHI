import os

# This script takes the preprocessed JSONL scenarios and actions as prompt completion pairs and uses them to fine tune a given open AI model
# It is based on https://platform.openai.com/docs/guides/fine-tuning
# TODO : Extend to other model providers

# Configuration
input_directory = "finetuning"
input_filename = "finetuning_training_data.json"
input_file = os.path.join( input_directory, input_filename )
openai_shell_cmd = f"openai tools fine_tunes.prepare_data -q -f {input_file}"

print( f"Executing shell command\n{openai_shell_cmd}\n\n")
# Prepare the data before fine tuning
os.system( openai_shell_cmd )