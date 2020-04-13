#!/usr/bin/python
from bs4 import BeautifulSoup
import os
from config import CHROME_DRIVER_PATH
from dateUtil import get_today_file_name
from selenium import webdriver
from upload_file_s3 import upload_file
file_name = get_today_file_name()

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches",["ignore-certificate-errors"])
options.add_argument('--disable-gpu')
options.add_argument('--headless')

root = os.path.dirname(__file__)

FILE_PATH = os.path.join(root, 'textfiles')


def extract_links_from_pages(page):
    soup = BeautifulSoup(page, "html.parser")
    file = open(FILE_PATH + file_name, 'a+')
    p = soup.findAll('div', attrs={'class': 'job-title-text'})
    for link in p:
        val = link.find_all('a')[0]
        file.write(val.get('href') + '\n')
        print(val.get('href'))


chrome_driver = CHROME_DRIVER_PATH
driver = webdriver.Chrome(chrome_driver, chrome_options= options)
driver.get("http://jobs.bdjobs.com/jobsearch.asp?fcatId=8")
extract_links_from_pages(driver.page_source)
import time
for x in range(1, 5):
    time.sleep(10)
    continue_link = driver.find_element_by_link_text(str(x))
    extract_links_from_pages(driver.page_source)
    continue_link.click()

driver.quit()
upload_file(file_name)