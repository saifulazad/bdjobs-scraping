__author__ = 'Azad'

import requests


def fetch_page(url):
    """
    Fetch and return page to caller
    :param url: A valid urls
    :return:
    """
    r = requests.get(url)

    return r.text