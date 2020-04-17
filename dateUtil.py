import datetime


def get_today_file_name():
    """
    This will return a string
    :return:
    """
    d = datetime.date.today()
    month = '%02d' % d.month
    day = '%02d' % d.day
    file_name = day + month + '.txt'
    return file_name
