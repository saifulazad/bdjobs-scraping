from jobpageprocess import fetch_page
from jobpageprocess.mapper import Mapper

if __name__ == '__main__':
    readfile = open("textfiles/1004.txt")
    r = readfile.readlines()
    for line in r:
        page = fetch_page('https://jobs.bdjobs.com/' + line)
        ob = Mapper(page=page)
        print(ob._read_from_HTML())

