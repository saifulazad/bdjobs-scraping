import datetime
import sys

from bs4 import BeautifulSoup
from config import WindowsEnvironment
from selenium import webdriver

import config
from dateUtil import get_today_file_name


file_name = get_today_file_name()
# file_name = 'link.txt'

def extract_links_from_pages(page):
    soup = BeautifulSoup(page, "html.parser")

    file = open(config.TXT_FILE_PATH +file_name, 'w+')
    p = soup.findAll('div', attrs={'class': 'job-title-text'})
    for link in p:
        val = link.find_all('a')[0]
        file.write(val.get('href') + '\n')
        print(val.get('href'))
    file.close()

try:
    for_windows = WindowsEnvironment()
except Exception as ex:
    print(ex)
    sys.exit()


chrome_driver = for_windows.get_path_with_driver()
driver = webdriver.Chrome(chrome_driver)
driver.get("http://jobs.bdjobs.com/jobsearch.asp?fcatId=8")
extract_links_from_pages(driver.page_source)
for x in range(2, 9):
    continue_link = driver.find_element_by_link_text(str(x))
    extract_links_from_pages(driver.page_source)
    continue_link.click()

driver.quit()