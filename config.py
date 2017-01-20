import platform
import os


class Environment(object):
    """
    This is the function that will work to select driver based on OS ('Windows', 'Linux')
    We are only supporting only 'Windows', 'Linux'. Hope next we will support OSX
    """

    PATH_WITH_DRIVER = ''

    def __init__(self, path=''):
        self.path = path or self.PATH_WITH_DRIVER

    def _has_driver(self):
        return os.path.isfile(self.file_path)

    def get_path_with_driver(self):
        if self._has_driver():
            return self.file_path
        else:
            raise FileNotFoundError('No chromedriver found at {0}.\n'
                                    'Please be sure you have configure PATH_WITH_DRIVER'.format(self.path))


class WindowsEnvironment(Environment):
    PATH_WITH_DRIVER = 'C:\\'

    def __init__(self, path=''):
        super(WindowsEnvironment, self).__init__(path=path)
        self.file_path = self.path + 'chromedriver.exe'


class LinuxEnvironment(object):
    PATH_WITH_DRIVER = '\\'

    def __init__(self, path=''):
        super(WindowsEnvironment, self).__init__(path=path)
        self.file_path = self.path + 'chromedriver'


def factory_for_os():
    os_name = platform.system()

    # List of OSs we are supporting now
    os_dict = {
        'Windows': WindowsEnvironment,
        'Linux': LinuxEnvironment
    }

    return os_dict.get(os_name, None)
