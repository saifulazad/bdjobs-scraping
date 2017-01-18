import datetime

from bs4 import BeautifulSoup
from data_analyzer.XLWritter import WritterXL
from dateUtil import get_today_file_name

from jobpageprocess import fetch_page
from jobpageprocess import Reader


class Mapper(object):
    """
         Main class who is responsible for processing a page
         Here page is BeautifulSoup's HTML page.
         We will parse each page in details and extract the
         information
    """

    def __init__(self, page):
        """
        Initializer to save precious information for future

        :param page: An HTML page is fetched by requests library
        :return:
        """

        # Those two dict hold useful information keys : class name of page
        #
        # Values are list as those class consist <li> elements
        #
        self.class_value_has_list = {
            'job_des': {
                'name': 'Job Description / Responsibility',
                'descriptions': []
            },
            'job_req': {
                'name': 'Job Requirements',
                'descriptions': []
            },
        }
        self.class_value_no_list = {
            'job-title': {
                'name': 'Job Title',
                'tag': 'h4'
            },
            'company-name': {
                'name': 'Job Title',
                'tag': 'h2'
            },
        }

        self.soup = BeautifulSoup(page, "html.parser") # Consume HTML page from requests library


    def _read_basic_info(self):
        """
        Read all basic information of a Job. job title and company name is vital
        :return dict: job title and company name as key value
        """
        for key in self.class_value_no_list:
            informations = self.soup.find(self.class_value_no_list[key]['tag'], attrs={'class': key})

            self.class_value_no_list[key]['info'] = informations.text.strip() # Store those as 'info' key

        return [self.class_value_no_list[key]['info'] for key in self.class_value_no_list.keys()]
        return self.class_value_no_list

    def _read_job_des_and_req(self):
        """
        A job has some description and responsibilities. Extract it for HTML page
        :return dict: job description and responsibilities as key value
        """
        for key in self.class_value_has_list.keys():
            informations = self.soup.findAll('div', attrs={'class': key})
            for information in informations:
                list_items = information.find('ul')

                for list_item in list_items.findAll('li'):
                    self.class_value_has_list[key]['descriptions'].append(list_item.text.strip())
        return self.class_value_has_list

    def _read_from_HTML(self, path=None):
        """
        This method to process whole job page. We are processing only 2 main parts of a page
        One is basic info and another is description and responsibilities
        Just call above 2 methods
        :param path:
        :return:
        """
        print(self._read_basic_info())
        print(self._read_job_des_and_req())
        return self._read_basic_info()


if __name__ == '__main__':

    val = (Reader('../link.txt').get_file_content())
    file_name = get_today_file_name().split('.')[0]
    print(file_name+ ".xlsx")
    xl_writter = WritterXL(file_name=file_name+ ".xlsx")
    for x in val[0:]:
        # print(x)
        page = fetch_page('http://jobs.bdjobs.com/' + x)
        ob = Mapper(page=page)
        xl_writter.write_to_file(ob._read_from_HTML())