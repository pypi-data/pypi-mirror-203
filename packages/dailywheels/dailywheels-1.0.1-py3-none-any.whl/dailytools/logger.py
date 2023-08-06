import os
import logging, logging.handlers


class Logger:
    def __init__(self, path, flevel=logging.INFO, clevel=logging.DEBUG, time_rotate=('M', 3), backupCount=14):
        LOG_DIR = os.path.dirname(path)
        os.makedirs(LOG_DIR, exist_ok=True)
        self.logger = logging.getLogger(__name__)
        # logging.Logger.manager.loggerDict.pop(__name__)
        # self.logger.handlers = []
        # self.logger.removeHandler(self.logger.handlers)
        if not self.logger.handlers:
            self.logger.setLevel(clevel)
            fmt = logging.Formatter("%(levelname)s:%(asctime)s - %(filename)s:%(lineno)d - %(message)s")

            # set Warning log file
            unit, circle = time_rotate
            self.fh = logging.handlers.TimedRotatingFileHandler(path, unit, circle, backupCount=backupCount)
            self.fh.setFormatter(fmt)
            self.fh.setLevel(clevel)

            # set cmd log
            self.sh = logging.StreamHandler()
            self.sh.setFormatter(fmt)
            self.sh.setLevel(clevel)

            self.logger.addHandler(self.fh)
            self.logger.addHandler(self.sh)

    def debug(self, message):
        self.__init__()
        self.logger.debug(message)
        self.logger.removeHandler(self.logger.handlers)

    def info(self, message):
        self.__init__()
        self.logger.info(message)
        self.logger.removeHandler(self.logger.handlers)

    def war(self, message):
        self.__init__()
        self.logger.warning(message)
        self.logger.removeHandler(self.logger.handlers)

    def error(self, message):
        self.__init__()
        self.logger.error(message)
        self.logger.removeHandler(self.logger.handlers)

    def cri(self, message):
        self.__init__()
        self.logger.critical(message)
        self.logger.removeHandler(self.logger.handlers)

    def get_logger(self):
        return self.logger



