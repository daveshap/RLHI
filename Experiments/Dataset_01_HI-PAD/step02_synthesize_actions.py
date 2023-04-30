import os
import yaml
import openai
from time import time, sleep
from random import seed, choice
from uuid import uuid4

seed()

def save_yaml(filepath, data):
    with open(filepath, 'w', encoding='utf-8') as file:
        yaml.dump(data, file, allow_unicode=True)

def open_file(filepath):
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as infile:
        return infile.read()

def save_file(filepath, content):
    with open(filepath, 'w', encoding='utf-8') as outfile:
        outfile.write(content)

def chatgpt_completion(messages, temp=0.7, model="gpt-3.5-turbo"):
    max_retry = 7
    retry = 0
    while True:
        try:
            response = openai.ChatCompletion.create(model=model, messages=messages, temperature=temp)
            text = response['choices'][0]['message']['content']
            return text
        except Exception as oops:
            retry += 1
            if retry >= max_retry:
                print(f"Exiting due to an error in ChatGPT: {oops}")
                exit(1)
            print(f'Error communicating with OpenAI: "{oops}" - Retrying in {2 ** (retry - 1) * 5} seconds...')
            sleep(2 ** (retry - 1) * 5)

if __name__ == "__main__":
    openai.api_key = open_file('key_openai.txt')
    scenario_folder = 'scenarios'
    action_folder = 'actions'
    action_metadata_folder = 'actions_metadata'
    
    system_message = open_file('system_action.txt')

    for scenario_file in os.listdir(scenario_folder):
        scenario_filepath = os.path.join(scenario_folder, scenario_file)
        action_filepath = os.path.join(action_folder, scenario_file)
        action_metadata_filepath = os.path.join(action_metadata_folder, scenario_file.split('.')[0] + '.yaml')

        if os.path.exists(action_filepath):
            continue

        scenario = open_file(scenario_filepath)
        messages = [
            {"role": "system", "content": system_message},
            {"role": "user", "content": scenario},
        ]
        action = chatgpt_completion(messages)
        print('\n\n===============\n\n\nScenario:\n', scenario, '\n\nAction:\n', action)
        #exit()
        save_file(action_filepath, action)

        metadata = {
            "original_scenario": scenario,
            "scenario_filepath": scenario_filepath,
            "action": action,
            "action_filepath": action_filepath,
            "system_message": system_message,
        }
        save_yaml(action_metadata_filepath, metadata)
