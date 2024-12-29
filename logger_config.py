import logging
from logging.handlers import RotatingFileHandler

class LoggerConfig:
    @staticmethod
    def get_logger(name="AlertLogger"):
        log_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        log_handler = RotatingFileHandler("alerts.log", maxBytes=5*1024*1024, backupCount=3)
        log_handler.setFormatter(log_formatter)
        log_handler.setLevel(logging.INFO)

        logger = logging.getLogger(name)
        logger.setLevel(logging.INFO)
        logger.addHandler(log_handler)
        return logger

logger = LoggerConfig.get_logger()
