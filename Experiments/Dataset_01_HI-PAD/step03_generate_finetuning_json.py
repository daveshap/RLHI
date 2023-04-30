import json
import os

# Configuration
scenarios_dir = "scenarios"
actions_dir = "actions"
output_directory = 'finetuning'
output_filename = "finetuning_training_data.json"
output_file = os.path.join( output_directory, output_filename )
records_processed = 0

OPENAI_PLATFORM = "openai"
platform_target = OPENAI_PLATFORM

#Open AI prepration config
# See for more details : https://platform.openai.com/docs/guides/fine-tuning/preparing-your-dataset
if platform_target == OPENAI_PLATFORM:
    prompt_separator = "\n\n###\n\n"
    completion_prefix = " "
    completion_suffix = "###"
else:
    # Add other targets here
    None


# Ensure the output directory exists
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

#Open the output JSON
jsonf = open(output_file, 'w')

# Scan all of the scenarios
for filename in os.listdir(scenarios_dir):
    if filename.endswith('.txt'):
        # Open and read the scenario file
        with open(os.path.join(scenarios_dir, filename), 'r') as f:
            scenario_text = f.read()

        # Get the UUID of the scenario
        # At the moment assumes all file names have the form scenario_<uuid>.txt
        uuid = filename[9:][:-4]

        # Open and read the corresponding actions file
        actions_filename = f"scenario_{uuid}.txt"
        with open(os.path.join( actions_dir, actions_filename), 'r') as f:
            action_text = f.read()


        # Write to the JSON file
        item = { "prompt" : f"{scenario_text}{prompt_separator}", "completion" : f"{completion_prefix}{action_text}{completion_suffix}" }
        jsonf.write(json.dumps(item) + "\n")
        records_processed += 1

jsonf.close()
print( f"Processed and wrote {records_processed} scenario records to {output_file}" )
