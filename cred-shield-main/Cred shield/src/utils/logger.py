import logging

class Logger:
    def __init__(self, name: str = "credshield"):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.INFO)
        handler = logging.FileHandler("credshield.log")
        formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

    def info(self, msg: str):
        self.logger.info(msg)

    def error(self, msg: str):
        self.logger.error(msg)

    def debug(self, msg: str):
        self.logger.debug(msg)
