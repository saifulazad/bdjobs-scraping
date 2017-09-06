import json
import re
import os, sys
# import pandas as pd

from copy import deepcopy, copy

from utils import get_non_dict_word

data_processor = lambda data_stream, job_id, list_key='oth_ben': \
    data_stream[job_id][list_key]['descriptions']

def read_company_info(data):
    l = []
    for key in data.keys():
        info = ([data[key][header_info]['info'] for header_info in ['job-title', 'company-name', 'company-info']])

        last_item = info[-1]

        if 'Follow' in last_item:
            last_item = last_item.replace('Follow', '')

            last_item = last_item.rstrip()

        l.append([info[1], info[0], last_item])

    l.sort()

    df = pd.DataFrame(l, columns=['Job tile', 'company-name', 'company-info'])
    for x in l:
        print(x[:-1])
        # df.to_html('./out.html',escape=False)
        # df.to_csv('./out.csv', sep='\t')


def get_firm_stack(json_data, ):
    all_job_descriptions = []
    for key in json_data.keys():
        try:
            # print(json_data[key])
            descriptions = data_processor(json_data, job_id=key, list_key='job_des')
            print(descriptions)
            all_job_descriptions.append(descriptions)
        except KeyError:
            (json_data[key])

    return deepcopy(all_job_descriptions)


def append_all_to_the_list(data_list):
    all_data = []
    unique_words = set()
    for job_des in data_list:
        all_data.extend(job_des)

    for x in all_data:

        lam = lambda x: re.split(r'[\W]', x)
        words = [p for p in lam(x) if len(p) > 0]

        for word in words:
            unique_words.add(word.lower())

    non_dict_word = get_non_dict_word(unique_words)
    has_unicode = lambda x: any([ord(c) > 128 for c in x])

    non_ba_words = [val for val in non_dict_word if not has_unicode(val)]
    print(non_ba_words)
    return copy(unique_words)


with open('./portfolio-6f471-export.json') as data_file:
    data_string = data_file.read()
    try:
        data = json.loads(data_string)
        print('Success!')
    except ValueError:
        print('Failed:')

# read_company_info(data=data['job'])
list_descriptions_for_each_job = get_firm_stack(json_data=data['job'])

append_all_to_the_list(list_descriptions_for_each_job)
