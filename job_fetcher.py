from dateUtil import get_today_file_name
from jobpageprocess import fetch_page, Reader
from jobpageprocess.mapper import Mapper
from firebase import firebase
from fire_base_config import CONFIG
import config
if __name__ == '__main__':

    txt_file_name = get_today_file_name()
    firebase = firebase.FirebaseApplication(CONFIG['URL'], None)
    read_file = config.TXT_FILE_PATH + txt_file_name

    val = (Reader(file_name=read_file).get_file_content())
    file_name = get_today_file_name().split('.')[0]
    for x in val[20:]:
        job_id = (x.split('id=')[1].split('&')[0])
        page = fetch_page('http://jobs.bdjobs.com/' + x)
        ob = Mapper(page=page)
        firebase.put('/job/', job_id, (ob._read_from_HTML()))
        print(job_id)
