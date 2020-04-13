__author__ = 'Azad'

import requests


def fetch_page(url):
    r = requests.get(url)

    return r.text