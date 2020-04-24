__author__ = 'Azad'

class Writter(object):
    pass


class Reader(object):
    """
    This is Reader class to read and process a .txt file and return URLS a list
    """
    def __init__(self, file_name):
        """

        :param file_name: A txt extension file
        :return:
        """
        self.file_list = open(file_name, 'r')

    def get_file_content(self):
        """

        :return list: list of ULS
        """
        urls = []
        while True:
            line = self.file_list.readline().strip()
            if line == '':
                break
            else:
                urls.append(line)

        return urls

if __name__ == "__main__":
    val = (Reader('../link.txt').get_file_content())
    print(val)

