

import os

# This script takes the preprocessed JSONL scenarios and actions as prompt completion pairs and uses them to fine tune a given open AI model
# It is based on https://platform.openai.com/docs/guides/fine-tuning
# TODO : Extend to other model providers
# NOTE: For this to run , you need to have set your OPENAI_API_KEY variable correctly

# Configuration
input_directory = "finetuning"
input_filename = "finetuning_training_data_prepared.jsonl"
input_file = os.path.join( input_directory, input_filename )
base_model = "ada"  # Just testing to keep costs down
openai_shell_cmd = f"openai api fine_tunes.create -t {input_file} -m {base_model}"

print( f"Executing shell command\n{openai_shell_cmd}\n\n")
# Prepare the data before fine tuning
os.system( openai_shell_cmd )
