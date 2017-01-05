import platform


os = platform.system()

golbal_os = ('Windows', 'Linux') # List of OSs we are supporting now

PATH_WITH_DRIVER = '' # Default PATH of chrome driver

def init_path():
    """
    This is the function that will work to select driver based on OS ('Windows', 'Linux')
    We are only supporting only 'Windows', 'Linux'. Hope next we will support OSX
    :return: True  if chrome driver found
    :Exception: otherwise
    """
    global PATH_WITH_DRIVER
    global os
    if os is 'Windows':
        PATH_WITH_DRIVER = 'C:\chromedriver.exe'
    elif os is 'Linux':
        PATH_WITH_DRIVER = ''

    import os.path
    is_consist = os.path.exists(PATH_WITH_DRIVER)

    if is_consist is True:
        return True
    else:
        raise Exception('No chromedriver found at {0}.\nPlease be sure you have configure PATH_WITH_DRIVER'.format(PATH_WITH_DRIVER))



if __name__ == "__main__":

    print(init_path())
    print(os)