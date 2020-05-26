#!/usr/bin/python
import os
import time

import boto3
from bs4 import BeautifulSoup
from selenium import webdriver

from dateUtil import get_today_file_name

BUCKET_NAME = 'jobstext'


def upload_file(file_name):
    s3 = boto3.client('s3')
    key = os.path.join('joblinksfile', os.path.basename(file_name))
    try:
        s3_response = s3.put_object(Bucket=BUCKET_NAME, Key=key, Body=open(file_name, 'rb'))
    except Exception as e:
        raise IOError(e)


root = os.path.dirname(__file__)
chrome_driver = os.path.join(root, 'chromedriver')
links_path = os.path.join(root, 'textfiles')
file_name = get_today_file_name()
file_to_write = os.path.join(links_path, file_name)

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["ignore-certificate-errors"])
options.add_argument('--disable-gpu')
options.add_argument('--headless')
driver = webdriver.Chrome(chrome_driver, chrome_options=options)

driver.get("http://jobs.bdjobs.com/jobsearch.asp?fcatId=8")


def extract_links_from_pages(page):
    file = open(file_to_write, 'a+')

    soup = BeautifulSoup(page, "html.parser")
    p = soup.findAll('div', attrs={'class': 'job-title-text'})
    for link in p:
        val = link.find_all('a')[0]
        file.write(val.get('href') + '\n')
        print(val.get('href'))


for x in range(1, 4):
    continue_link = driver.find_element_by_link_text(str(x))
    time.sleep(10)
    extract_links_from_pages(driver.page_source)
    continue_link.click()

driver.quit()
upload_file(file_to_write)
