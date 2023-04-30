import os
import json


prompt_dir = 'scenarios/'
completion_dir = 'actions/'


def open_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as infile:
        return infile.read()


if __name__ == '__main__':
    files = os.listdir(prompt_dir)
    data = list()
    for file in files:
        prompt = open_file(prompt_dir + file)
        completion = open_file(completion_dir + file)
        info = {'prompt': prompt + '\n\nRESPONSE:\n', 'completion': completion + ' STOP STOP STOP'}
        data.append(info)
    with open('hi-pad.jsonl', 'w', encoding='utf-8') as outfile:
        for i in data:
            json.dump(i, outfile)
            #json.dump(i, outfile, ensure_ascii=False)
            outfile.write('\n')