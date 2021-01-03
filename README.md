
# bdjobs-scraping [DO NOT FOLLOW IT NOW]
## Introduction 
Scraping is a hot topic nowadays. This is a demo about my scraping skill. [bdjobs](http://jobs.bdjobs.com/jobsearch.asp?fcatId=8) is the largest job posting site in Bangladesh. We are only concern on IT-related jobs.

## Libraries and language used in this project
* python 3.X
* Beautifulsoup
* requests 
* selenium
* boto3

## How does it work:

* Run `BDjobs_click.py`. 

* We are using selenium to automate the scraping process. 

* Selenium will click the page one by one and pass the page to Beautifulsoup.

* Beautifulsoup will extract the URLs from the pages.

* After extracting the URL (job details page link) we pass that link to requests.

* By using requests module we fetch the job details page.

* After getting page we parse it and extract all useful info from that page.

## How to start 

* Clone the project 
* Open terminal then `cd bdjobs-scraping` and hit Enter    
* Download [chromedriver](https://sites.google.com/a/chromium.org/chromedriver/) in project root folder. Make sure it matches with your current chrome browser version
* You can start by virtual env (optional)
* At terminal `python -m pip install -r requiriement.txt`
* Edit the config.py file provide PATH of your chrome driver
  * For windows, our default path is C drive. So keep chrome driver at C: drive
* run `bdjobs_click.py` and wait a bit to complete the process 
* There will be a txt file at *textfiles* folder named with ddmm.txt. 
* If above process works good one can see many links on that page.
* Then run the `mapper.py` located on *jobpageprocess* package.

## How to set crontab

 * `0 0 */7 * *` run after 7 Days at 12:00
 * after set cron need to restart cron server use `sudo service cron reload` in ubuntu.
 * 0 0 * * * /usr/bin/python /var/www/html/crontest/cron.py >>/dev/null 2>&1
  
### TODOs
- [x] run selenium and extract the links
- [x] run each link and scrape particular job
- [x] Write documentation 
- [ ] Analysis of data by Machine Learning


### Contact
> Facebook https://www.facebook.com/mr.saiful.azad

> Gmail mr.saiful.azad@gmail.com
