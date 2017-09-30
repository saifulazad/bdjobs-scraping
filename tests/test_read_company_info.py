import unittest

from data_analyzer.read_copany_info import make_key_value, process_meta_info,\
    make_tuple_to_words_set


class TestReadCompanyInfo(unittest.TestCase):
    def setUp(self):
        self.data_web = 'Web : www:nokia.com'
        self.data_business = 'Business : Telephony'
        self.data_address = 'Address : Global'

        self.invalid_data = 'Invalid : Invalid'

        self.meta_data = '\n\n'.join([self.data_web,self.data_address, self.data_business])


        self.data_tuple = ('This is a data', 'This is another:, data')

    def test_make_key_value(self):
        self.assertEqual(make_key_value(self.data_web), {'web':'www:nokia.com'})

    def test_invalid_data_input(self):
        self.assertEqual(make_key_value(self.invalid_data), {})

    def test_process_meta_info(self):
        self.assertEqual(process_meta_info(self.meta_data), {'web':'www:nokia.com', 'address':
                                                              'Global', 'business': 'Telephony'})
    def test_process_meta_info_empty(self):
        self.assertEqual(process_meta_info(self.invalid_data), {})

    def test_make_tuple_to_words_set(self):
        self.assertEqual(make_tuple_to_words_set(self.data_tuple), {
            'this', 'is', 'a', 'data', 'another'
        })
    def test_make_tuple_to_words_set_empty(self):
        self.assertEqual(make_tuple_to_words_set(tuple()), set())

    def test_get_job_des_and_requirements(self):
        pass

