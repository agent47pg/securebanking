import logging
import datetime
import os
from os.path import dirname, join, abspath

class SingletonType(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(SingletonType, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class BankLogger(object, metaclass=SingletonType):
    _logger = None

    def __init__(self):
        #ideally logger_name should be child class name
        logger_name = "SecureBank"
        self._logger = logging.getLogger(logger_name)
        self._logger.setLevel(logging.DEBUG)
        log_file_format = "[%(levelname)s] - %(asctime)s - %(name)s - : %(message)s in %(pathname)s:%(lineno)d"
        formatter = logging.Formatter(log_file_format)

        now = datetime.datetime.now()
        log_dir = abspath(join(dirname(__file__), '../log'))

        if not os.path.isdir(log_dir):
            os.mkdir(log_dir)
        fileHandler = logging.FileHandler(log_dir + "/log_" + now.strftime("%Y-%m-%d")+".log")
        streamHandler = logging.StreamHandler()
        fileHandler.setFormatter(formatter)
        streamHandler.setFormatter(formatter)

        self._logger.addHandler(fileHandler)
        self._logger.addHandler(streamHandler)

    def get_logger(self):
        return self._logger
