import json
import re

from data_analyzer.utils import get_non_dict_word, tags


def make_key_value(data_pair):
    data_looking_for = {'Web', 'Business', 'Address', }
    data = data_pair.split(':', 1)
    if len(data) == 2 and (data[0].strip() in data_looking_for):
        return {data[0].strip().lower(): data[1].strip()}
    return {}


def process_meta_info(data_str):
    data_dict = {}
    for item in data_str.splitlines():
        data_dict.update(make_key_value(item))
    return data_dict


def read_company_info(data, file_to_save=None):
    jobs = []
    for key in data.keys():
        info = ([data[key][header_info]['info'] for header_info in
                 ['job-title', 'company-name', 'company-info']])

        last_item = info[-1]
        info_basic = ({'company_name': info[1], 'job_title': info[0]}) or {}
        meta_data = (process_meta_info(last_item)) or {}

        jobs.append({**info_basic, **meta_data, 'tech_stacks':
            get_tech_stack(data[key], format='dict')})

        print({**info_basic, **meta_data, 'tech_stacks':
            get_tech_stack(data[key], format='dict')})
    if file_to_save:
        with open(file_to_save + '.txt', 'w') as outfile:
            json.dump(jobs, outfile)


def get_tech_stack(data, format='dict'):
    job_des_req = get_job_des_and_requirements(data)

    word_set = (make_tuple_to_words_set(job_des_req['job_req_and_des']))

    non_dict_word = get_non_dict_word(word_set)

    only_tag = non_dict_word & tags

    if format == 'dict':
        return [{'tag_name': tag} for tag in only_tag]
    else:
        return only_tag


def get_job_des_and_requirements(data):
    descriptions = tuple()
    requirements = tuple()
    try:
        descriptions = tuple(data['job_des']['descriptions'])
    except KeyError as ex:
        print("----------------ERROR START---------------")
        print(data)
        print("Has no key {0} or {1}".format('job_des', 'descriptions'))
        print("----------------ERROR END ---------------")
    try:
        requirements = tuple(data['job_req']['descriptions'])
    except KeyError as ex:
        print("----------------ERROR START---------------")
        print(data)
        print("Has no key {0} or {1}".format('job_req', 'descriptions'))
        print("----------------ERROR END ---------------")

    return {
        'job_descriptions': descriptions,
        'job_requirements': requirements,
        'job_req_and_des': requirements + descriptions
    }


def make_tuple_to_words_set(data_tuple):
    lam = lambda x: re.split(r'[\W]', x)
    words_set = set()
    for sentance in data_tuple:
        assert isinstance(sentance, str)

        words = [p.lower() for p in lam(sentance) if len(p) > 0]
        words_set.update(words)
    return words_set


if __name__ == '__main__':

    with open('./portfolio-6f471-export.json') as data_file:
        data_string = data_file.read()
        try:
            data = json.loads(data_string)
            # print('Success!')
        except ValueError:

            print('Failed:')

    read_company_info(data=data['job'], file_to_save='jobs')
