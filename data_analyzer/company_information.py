import json
import re
import sys
from tag_analytic.tag import valid_tags


pattern = {
    'name': r'Company Information\n(.*)\n',
    'web': r'Web : (.*)\n',
    'address': r'Address : (.*)\n',
    'business': r'Business : (.*)\n'
}


with open(sys.argv[1]) as json_data:
    company_information = json.load(json_data)
companies_information_list = []


for jobs in company_information:
    company_info = (jobs["company-info"]["info"])
    position = (jobs["job-title"]["info"])
    companies_data = {}
    for key, value in pattern.items():
        job_information = re.search(value, company_info)
        if job_information:
            companies_data[key] = job_information.groups()[0]


    class my_dictionary(dict):
        def __init__(self):
            self = dict()

        def add(self, key, value):
            self[key] = value


    dict_obj = my_dictionary()
    dict_obj.add('company', companies_data)
    dict_obj.add('position', position)
    dict_obj.add('stack', valid_tags(data=jobs))
    companies_information_list.append(dict_obj)

print(json.dumps(companies_information_list, indent=4))

#python company_information.py ../