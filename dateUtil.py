import datetime

def get_today_file_name():
    """
    This will return a string
    :return:
    """
    d = datetime.date.today()
    month = '%02d' % d.month
    day = '%02d' % d.day
    file_name = day+month+ '.txt'
    return file_name

def get_yesterday_file_name():

    d = datetime.date.today() - datetime.timedelta(days=1)
    month = '%02d' % d.month
    day = '%02d' % d.day
    file_name = day+month+ '.txt'
    return file_name


if __name__ == '__main__':
    print(get_today_file_name())
    print(get_yesterday_file_name())
