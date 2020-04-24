import json
import re
data = open("/home/azad/gitrepos/bdjobs-scraping/data.json")
data = json.loads(data.read())
for job in data:
    company_info = (job["company-info"]["info"])
    info = {}
    for benefites
    print(info)