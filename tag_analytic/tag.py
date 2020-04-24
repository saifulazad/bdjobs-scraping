import csv
import json
from nltk.tag import pos_tag
from nltk.tokenize import word_tokenize

all_data = open("/home/azad/gitrepos/bdjobs-scraping/data.json")  # Open and read all data from json file.
data = json.loads(all_data.read())
tags = set()

with open('/home/azad/gitrepos/bdjobs-scraping/data_analyzer/tags_mini.csv') as csvfile:  # Get all teg from csv file.
    reader = csv.DictReader(csvfile)
    for row in reader:
        y = (row['tagName'])
        if int(row['count']) < 2000:
            break
        tags.add(y)


def get_words_from_sentance(sentance):
    return sentance.split()


def lower_case_words(words):
    lower_case_words = []
    for word in words:
        lower_word = word.lower()
        lower_case_words.append(lower_word)

    return lower_case_words


def is_valid_tag(tag):
    return tag in tags


def valid_tag(data):
    for x in data:
        tag_list = []
        for job_req in (x["job_req"]["descriptions"]):
            tagged_sent = pos_tag(word_tokenize(job_req))
            adjective = [word for word, pos in tagged_sent if pos == 'NNP' and is_valid_tag(word.lower())]
            tag_list.extend(adjective)
        tag = (list(set(tag_list)))
        technology = tag
        my_json_string = json.dumps(technology)
        print(my_json_string)


valid_tag(data=data)
