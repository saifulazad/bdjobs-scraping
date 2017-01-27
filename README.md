# bdjobs-scraping
##Introduction 
Scraping is a hot topic now a days. This is a demo about my scraping skill. [bdjobs](http://jobs.bdjobs.com/jobsearch.asp?fcatId=8) is the largest job posting site in Bangladesh. We are only concern on IT related jobs.

##How does it work:

After running that `BDjobs_click.py`. 

* We are using selenium to automate the scraping process. 

* Selenium will click the page one by one and pass the page to Beautifulsoup.

* Beautifulsoup will extact the urls from the pages.

* After extracting the url (job details page link) we pass that link to requests.

* By using requests module we fetch the job details page.

* After getting page we parse it and extact all useful info from that page.

##Libararies and language used in this project
* python 3.X
* Beautifulsoup
* requests 
* selenium

##How to start 
* You can start by virtual env (optional)
* `python -m pip install -r requiriement.txt`
* Edit the config.py file provide PATH of your chrome driver 
* run `BDjobs_click.py`

  
###TODOs
- [x] run selenium and extract the links
- [x] run each link and scrape perticlar job
- [x] Write documentation 
- [ ] Analysis of data by Machine Learing 
