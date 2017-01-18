from jobpageprocess.fetcher import Reader

__author__ = 'Azad'

def file_to_read(file_name):

    first_file  = Reader(file_name)

    links = set(first_file.get_file_content())
    return links


def links_to_process(file_name, today_file, yesturday_file):

    file = file_to_read(today_file)
    another_file  = file_to_read(yesturday_file)

    links = file - another_file
    file = open(file_name, 'w+')
    for link in links:
        file.write(link + '\n')
    # return links


if __name__ == '__main__':
    print(links_to_process('asas','1801.txt', '1701.txt'))