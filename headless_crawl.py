# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# options = Options()
# options.set_headless(headless=True)
# driver = webdriver.Chrome(chrome_options=options, executable_path='./chromedriver')
# driver.get("http://google.com/")
# print ("Headless Chrome Initialized on Linux OS")

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches",["ignore-certificate-errors"])
options.add_argument('--disable-gpu')
options.add_argument('--headless')
driver = webdriver.Chrome(executable_path='./chromedriver', chrome_options=options)
driver.get("http://google.com/")
print ("Headless Chrome Initialized")
driver.quit()