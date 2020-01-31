import logging


class LoggingBase(object):

    def __init__(self):
        logging.basicConfig()
        self.logger = logging.getLogger(self.__class__.__name__)
        self.logger.setLevel(logging.INFO)
