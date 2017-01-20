from config import WindowsEnvironment
import unittest


class TestDriverPath(unittest.TestCase):
    def setUp(self):
        self.windows_driver = 'chromedriver.exe'
        self.windows_default_path = WindowsEnvironment.PATH_WITH_DRIVER
        self.windows_custom_path = 'C:\\Users\\Azad\\Desktop\\'

    def test_for_os_environment_success_default_path(self):
        windows_path = WindowsEnvironment()
        file_path = windows_path.get_path_with_driver()
        self.assertEqual(file_path, self.windows_default_path + self.windows_driver)

    def test_for_os_environment_success_custom_path(self):
        windows_path = WindowsEnvironment(path=self.windows_custom_path)
        file_path = windows_path.get_path_with_driver()
        self.assertEqual(file_path, self.windows_custom_path + self.windows_driver)
    def test_for_os_environment_failure_default_path(self):
        windows_path = WindowsEnvironment()
        self.assertRaises(Exception,windows_path.get_path_with_driver())
    def test_for_os_environment_failure_custom_path(self):
        pass


if __name__ == '__main__':
    unittest.main()