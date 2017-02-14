from bs4 import BeautifulSoup

import config
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
            'oth_ben': {
                'name': 'Other Benefits',
                'descriptions': []
            },
        }
        self.class_value_no_list = {
            'job-title': {
                'name': 'Job Title',
                'tag': 'h4'
            },
            'company-name': {
                'name': 'Company Name',
                'tag': 'h2'
            },

            'company-info': {
                'name': 'Company Information',
                'tag': 'div'
            },

        }

        self.soup = BeautifulSoup(page, "html.parser")  # Consume HTML page from requests library


    def _read_basic_info(self):
        """
        Read all basic information of a Job. job title and company name is vital
        :return dict: job title and company name as key value
        """
        for key in self.class_value_no_list:
            informations = self.soup.find(self.class_value_no_list[key]['tag'], attrs={'class': key})

            self.class_value_no_list[key]['info'] = informations.text.strip()  # Store those as 'info' key

        return [self.class_value_no_list[key]['info'] for key in self.class_value_no_list.keys()]
        # return self.class_value_no_list

    def _read_job_des_and_req(self):
        """
        A job has some description and responsibilities. Extract it for HTML page
        :return dict: job description and responsibilities as key value
        """
        for key in self.class_value_has_list.keys():
            try:
                informations = self.soup.findAll('div', attrs={'class': key})
                for information in informations:
                    list_items = information.find('ul')

                    for list_item in list_items.findAll('li'):
                        self.class_value_has_list[key]['descriptions'].append(list_item.text.strip())
            except:
                pass
        return self.class_value_has_list

    def _read_from_HTML(self, path=None):
        """
        This method to process whole job page. We are processing only 2 main parts of a page
        One is basic info and another is description and responsibilities
        Just call above 2 methods
        :param path:
        :return:
        """
        # print(self._read_basic_info())
        print(self._read_job_des_and_req())

        all_list_info = self._read_job_des_and_req()
        total_des = []
        for key in self.class_value_has_list.keys():
            description = all_list_info[key]['descriptions']
            # print(description)
            description.extend([''] * (100 - len(description)))
            print(description)
            total_des.extend(description)
        basic_info_list = self._read_basic_info()

        basic_info_list.extend(total_des)
        return basic_info_list


if __name__ == '__main__':

    txt_file_name = get_today_file_name()

    read_file = config.TXT_FILE_PATH + txt_file_name

    val = (Reader(file_name=read_file).get_file_content())

    print(val)
    file_name = get_today_file_name().split('.')[0]
    file_name = config.XLSX_PATH + file_name + ".xlsx"
    xl_writter = WritterXL(file_name=file_name)
    for x in val[20:]:
        print(x)
        page = fetch_page('http://jobs.bdjobs.com/' + x)
        ob = Mapper(page=page)

        xl_writter.write_to_file(ob._read_from_HTML())