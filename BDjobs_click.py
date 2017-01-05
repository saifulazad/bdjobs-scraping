__author__ = 'Azad'
import sys

from bs4 import BeautifulSoup
from selenium import webdriver

import config

try:
    config.init_path()
except Exception as ex:
    print(ex)
    sys.exit()
file = open('link.txt', 'a')

def extract_links_from_pages(page):
    soup = BeautifulSoup(page, "html.parser")

    p = soup.findAll('div', attrs={'class': 'job-title-text'})
    for link in p:
        val = link.find_all('a')[0]
        file.write(val.get('href') + '\n')
        print(val.get('href'))


chrome_driver = config.PATH_WITH_DRIVER

driver = webdriver.Chrome(chrome_driver)
driver.get("http://jobs.bdjobs.com/jobsearch.asp?fcatId=8")
extract_links_from_pages(driver.page_source)
for x in range(2, 9):
    continue_link = driver.find_element_by_link_text(str(x))
    extract_links_from_pages(driver.page_source)
    continue_link.click()

driver.quit()