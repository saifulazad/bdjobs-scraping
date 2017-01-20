from dateUtil import get_today_file_name, get_yesterday_file_name
import unittest


class TestDateUtilMethod(unittest.TestCase):
    def setUp(self):
        self.today_file = '2001.txt'
        self.yesturday_file = '1901.txt'

    def test_get_today_file_name(self):
        self.assertEqual(get_today_file_name(), self.today_file)

    def test_get_yesterday_file_name(self):
        self.assertEquals(get_yesterday_file_name(), self.yesturday_file)

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()