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

def read_list(filepath):
    content = open_file(filepath)
    return content.strip().split('\n')

def chatgpt_completion(messages, temp=0.7, model="gpt-3.5-turbo"):
    max_retry = 7
    retry = 0
    while True:
        try:
            response = openai.ChatCompletion.create(model=model, messages=messages, temperature=temp)
            text = response['choices'][0]['message']['content']
            #filename = 'chat_%s_muse.txt' % time()
            #if not os.path.exists('chat_logs'):
            #    os.makedirs('chat_logs')
            #save_file('chat_logs/%s' % filename, text)
            return text
        except Exception as oops:
            retry += 1
            if retry >= max_retry:
                print(f"Exiting due to an error in ChatGPT: {oops}")
                exit(1)
            print(f'Error communicating with OpenAI: "{oops}" - Retrying in {2 ** (retry - 1) * 5} seconds...')
            sleep(2 ** (retry - 1) * 5)

def generate_scenario(list_scope, list_severity, list_category, list_domain, list_entropy, list_region):
    scope = choice(list_scope)
    severity = choice(list_severity)
    category = choice(list_category)
    domain = choice(list_domain)
    entropy = choice(list_entropy)
    region = choice(list_region)
    return f"Random word: {entropy}\nScope: {scope}\nSeverity: {severity}\nRegion: {region}\nCategory: {category}\nDomain: {domain}\n"

if __name__ == "__main__":
    openai.api_key = open_file('key_openai.txt')
    
    list_scope = read_list('list_scope.txt')
    list_region = read_list('list_region.txt')
    list_severity = read_list('list_severity.txt')
    list_category = read_list('list_category.txt')
    list_domain = read_list('list_domain.txt')
    list_entropy = read_list('list_entropy.txt')
    list_system = read_list('list_system.txt')

    for i in range(2000):
        default_system = choice(list_system)
        scenario_id = str(uuid4())
        scenario = generate_scenario(list_scope, list_severity, list_category, list_domain, list_entropy, list_region)
        messages = [
            {"role": "system", "content": default_system},
            {"role": "user", "content": scenario},
        ]
        response = chatgpt_completion(messages)
        print('\n\n===============\n\n\nScenario:\n', scenario, '\n\nResponse:\n', response)
        filepath = 'scenarios/scenario_%s.txt' % scenario_id
        save_file(filepath, response)
        # save metadata
        filepath = filepath.replace('scenarios','scenario_metadata').replace('.txt','.yaml')
        scenario_attributes = yaml.safe_load(scenario)
        scenario_attributes['Scenario'] = scenario_id
        scenario_attributes['System'] = default_system
        save_yaml(filepath, scenario_attributes)
        #exit()