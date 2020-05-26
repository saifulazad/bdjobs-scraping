import csv
from nltk.tag import pos_tag
from nltk.tokenize import word_tokenize

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


def valid_tags(data):
    tag_list = []
    for job_req in (data["job_des"]["descriptions"]):
        tagged_sent = pos_tag(word_tokenize(job_req))
        print(tagged_sent)
        adjective = [word for word, pos in tagged_sent if pos == 'NNP' and is_valid_tag(word.lower())]
        tag_list.extend(adjective)
    for job_req in (data["job_req"]["descriptions"]):
        tagged_sent = pos_tag(word_tokenize(job_req))
        # print(tagged_sent)
        adjective = [word for word, pos in tagged_sent if pos == "NNP" and is_valid_tag(word.lower())]
        tag_list.extend(adjective)
    tag = (list(set(tag_list)))
    return tag


if __name__ == "__main__":
    tag = valid_tags(data={
      "job_des":{
         "name":"Job Description / Responsibility",
         "descriptions":[
            "Answer customer service inquiries by receiving chats, emails, and managing incoming calls (if needed).",
            "Handling customer's complaints, providing appropriate solutions, and alternatives through chats.",
            "Using critical thinking to ask customers targeted questions to quickly understand the root of the problem.",
            "Identifying and assessing customer's needs to achieve satisfaction.",
            "Handling YouTrack tickets associated with customer's request and issues.",
            "Talk clients through a series of actions, either via phone, email, or chat, until they've solved a technical issue.",
            "Build sustainable relationships and trust with customer accounts through open and interactive communication.",
            "Drive platform adoption and offer best practice tips to help clients effectively meet their business goals.",
            "Properly escalate unresolved issues to appropriate internal teams (e.g. software developers).",
            "Provide prompt and accurate feedback to customers by using the right methods/tools.",
            "Refer to internal database or external resources to provide accurate tech solutions.",
            "Ensure all issues are properly logged.",
            "Prioritize and manage several open issues at one time.",
            "Follow up with clients to ensure their IT systems are fully functional after troubleshooting.",
            "Prepare accurate and timely reports.",
            "Document technical knowledge in the form of notes, articles and manuals.",
            "Maintain jovial relationships with clients."
         ]
      },
      "job_req":{
         "name":"Job Requirements",
         "descriptions":[
            "Strong written and oral communication skills in English is a must.",
            "Must be articulate, organized, and detail-oriented.",
            "Willingness to work as per roaster.",
            "Hard working.",
            "Good interpersonal skills.",
            "Strong business acumen, ethics and high integrity."
         ]
      },
      "oth_ben":{
         "name":"Other Benefits",
         "descriptions":[
            "Mobile bill, Performance bonus, Weekly 2 holidays, Insurance",
            "Lunch Facilities: Full Subsidize",
            "Festival Bonus: 2"
         ]
      },
      "job-title":{
         "info":"Technical Support Engineer"
      },
      "company-name":{
         "info":"IdeaScale Bangladesh"
      },
      "company-info":{
         "info":"Company Information\nIdeaScale Bangladesh\nAddress : Quantum Mustafa Tower (Floor: 4&5) 18, Gaus-ul-Azam Avenue, Sector-13 Uttara, Dhaka\nWeb : www.ideascale.com\nBusiness : IdeaScale is the largest cloud-based innovation software platform in the world with more than 25,000 customers and 4.5 million users. The software allows organizations to involve the opinions of public and private communities by collecting their ideas and giving users a platform to vote. The ideas are then evaluated, routed, and implemented, making IdeaScale the engine of crowd-powered innovation. IdeaScale\u2019s client roster includes industry leaders, such as Citrix, Marriott Vacations Worldwide, NASA, the New York City Police Department, Princess Cruises and many others.\n\n\n\u00a0Follow"
      },
      "url":"jobdetails.asp?id=905134&fcatId=8&ln=1",
      "created_at":1589501468
   })
    print(tag)
